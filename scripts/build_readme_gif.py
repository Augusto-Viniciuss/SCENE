"""Build the generic README illustration with Python's stdlib and FFmpeg/librsvg."""

from html import escape
import json
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'docs/media/scene-workflow.gif'
WIDTH, HEIGHT, FPS, DURATION = 1120, 560, 10, 9
LABELS = ['Research inputs', 'Story + script', 'Method in SVG', 'Demos + results', 'Narrated video']
CAPTIONS = [
    'Read the paper. Inspect the recordings.',
    'Shape the story before building the scenes.',
    'Explain the mechanism with SVG animation.',
    'Connect demonstrations with traceable results.',
    'Align the narration. Review the final export.',
]


def text(x, y, value, size=18, fill='#e8edf4', anchor='start', weight=400):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{escape(value)}</text>')


def icon(index, progress):
    if index == 0:
        lines = ''.join(f'<path d="M23 {y}h{length * progress:.1f}"/>'
                        for y, length in [(30, 31), (42, 25), (54, 28)])
        return f'<path d="M14 9h34l15 15v46H14zM48 9v15h15"/>{lines}<rect x="48" y="47" width="38" height="28" rx="4" fill="#111b25"/><path d="m62 55 12 6-12 6z"/>'
    if index == 1:
        bars = ''.join(f'<path d="M22 {y}h{length * progress:.1f}"/>'
                       for y, length in [(24, 37), (37, 46), (50, 29)])
        return f'<rect x="11" y="10" width="74" height="61" rx="5"/>{bars}<path d="M17 82h62M24 77v10M49 77v10M73 77v10"/>'
    if index == 2:
        return (f'<path d="M23 49 47 23l26 26-26 24z" stroke-dasharray="150" stroke-dashoffset="{150 * (1-progress):.1f}"/>'
                '<circle cx="23" cy="49" r="7" fill="#111b25"/><circle cx="47" cy="23" r="7" fill="#111b25"/>'
                '<circle cx="73" cy="49" r="7" fill="#111b25"/><circle cx="47" cy="73" r="7" fill="#111b25"/>')
    if index == 3:
        return (f'<rect x="8" y="14" width="48" height="39" rx="4"/><path d="m27 25 12 8-12 8zM47 79h42"/>'
                f'<path d="M56 77v{-25 * progress:.1f}m12 {25 * progress:.1f}v{-43 * progress:.1f}m12 {43 * progress:.1f}v{-34 * progress:.1f}"/>')
    waves = ''.join(f'<path d="M{x} {75-h*progress/2:.1f}v{h*progress:.1f}"/>'
                    for x, h in [(20, 8), (28, 18), (36, 28), (44, 14), (52, 24), (60, 32), (68, 18), (76, 8)])
    return f'<rect x="8" y="8" width="80" height="51" rx="5"/><path d="m38 21 18 12-18 12z"/>{waves}'


def frame_svg(t):
    current = min(int(t / 1.6), 4)
    complete = t >= 8
    progress = min(max((t - current * 1.6) / 1.3, 0), 1)
    progress = progress * progress * (3 - 2 * progress)
    body = text(48, 66, 'SCENE', 38, weight=700)
    body += text(1072, 61, 'RESEARCH, EXPLAINED.', 14, '#9caabc', 'end')
    body += text(48, 112, 'An academic video workflow for AI agents', 22, '#9caabc')
    body += text(48, 182, f'{current+1:02d} / {CAPTIONS[current]}', 26)
    for index, label in enumerate(LABELS):
        x = 48 + index * 212
        active = index == current and not complete
        done = index < current or complete
        border = '#67e8f9' if active else '#344254' if done else '#253142'
        color = '#67e8f9' if active else '#c3d0df' if done else '#64748b'
        body += f'<rect x="{x}" y="226" width="180" height="204" rx="14" fill="#111b25" stroke="{border}" stroke-width="2"/>'
        body += text(x+17, 254, f'{index+1:02d}', 12, color)
        body += (f'<g transform="translate({x+42} 273)" stroke="{color}" stroke-width="2.6" '
                 'stroke-linecap="round" stroke-linejoin="round" fill="none">'
                 + icon(index, progress if active else 1 if done else 0) + '</g>')
        body += text(x+90, 400, label, 18, '#e8edf4', 'middle')
        if done:
            body += f'<path d="m{x+147} 250 4 4 8-9" fill="none" stroke="#67e8f9" stroke-width="2"/>'
        if index < 4:
            body += f'<path d="M{x+191} 327h12l-4-4m4 4-4 4" fill="none" stroke="#64748b" stroke-width="2"/>'
    position = 138 + (4 if complete else min(current + progress, 4)) * 212
    body += '<path d="M138 472H986" stroke="#253142" stroke-width="3"/>'
    body += f'<path d="M138 472H{position:.1f}" stroke="#67e8f9" stroke-width="3"/>'
    for index in range(5):
        color = '#67e8f9' if index <= current else '#344254'
        body += f'<circle cx="{138+index*212}" cy="472" r="5" fill="{color}"/>'
    body += text(48, 529, 'Generic illustration · No research data', 14, '#9caabc')
    body += text(1072, 529, 'PAPER → STORY → METHOD → EVIDENCE → VIDEO', 12, '#9caabc', 'end')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
            f'viewBox="0 0 {WIDTH} {HEIGHT}"><rect width="100%" height="100%" fill="#070c13"/>'
            f'<g font-family="DejaVu Sans,sans-serif">{body}</g></svg>')


def main():
    decoders = subprocess.run(['ffmpeg', '-hide_banner', '-decoders'], capture_output=True, text=True, check=True)
    if 'librsvg' not in decoders.stdout:
        raise SystemExit('This optional asset builder needs FFmpeg with the librsvg decoder.')
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='scene-readme-') as folder:
        for number in range(FPS * DURATION):
            svg = frame_svg(number / FPS)
            ET.fromstring(svg)
            (Path(folder) / f'frame-{number:03d}.svg').write_text(svg, encoding='utf-8')
        result = subprocess.run([
            'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-filter_complex_threads', '1',
            '-framerate', str(FPS), '-i', str(Path(folder) / 'frame-%03d.svg'),
            '-filter_complex', '[0:v]split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];'
            '[b][p]paletteuse=dither=bayer:bayer_scale=3:diff_mode=rectangle',
            '-loop', '0', str(OUTPUT),
        ], capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stderr[-2000:])
    probe = json.loads(subprocess.check_output([
        'ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_frames',
        '-show_entries', 'stream=width,height,nb_read_frames,duration', '-of', 'json', str(OUTPUT),
    ], text=True))['streams'][0]
    assert (probe['width'], probe['height']) == (WIDTH, HEIGHT)
    assert int(probe['nb_read_frames']) == FPS * DURATION
    assert abs(float(probe['duration']) - DURATION) < 1 / FPS
    assert 0 < OUTPUT.stat().st_size < 2_000_000, 'Keep the README asset below 2 MB.'
    print(f'{OUTPUT.relative_to(ROOT)}: {WIDTH}×{HEIGHT}, {DURATION}s, {OUTPUT.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()

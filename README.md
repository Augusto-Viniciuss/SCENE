# SCENE Kit

**Scientific Communication through Explanation, Narration and Evidence.**

**English** | [Portuguese (Brazil)](README.pt-BR.md)

Reusable instructions for academic videos that explain a method, show demonstrations, present traceable results, and include narration. The agent uses HyperFrames for composition, FFmpeg for media operations, and optionally VoiceStudio for speech.

This repository is a documentation kit and an agent skill. It contains no papers, recordings, examples from real research, or custom rendering engine.

## Which file does what?

| File | Purpose |
|---|---|
| [README.md](README.md) / [README.pt-BR.md](README.pt-BR.md) | Installation, dependencies, and starting a project. |
| [AGENTS.md](AGENTS.md) | Standing instructions for agents working in this repository. |
| [SKILL.md](.agents/skills/scene/SKILL.md) | Portable workflow, invoked with `$scene`. |
| [Production guide](.agents/skills/scene/references/production.md) | Visual direction, evidence, editing, voice, and verification. |
| [Brief template](.agents/skills/scene/assets/BRIEF.template.md) | Information specific to each video. |

The conventional skill filename is **`SKILL.md`, singular**, inside its own directory. `AGENTS.md` and a skill complement each other: one guides work in the repository; the other carries the production workflow to other projects. See the official documentation for [AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) and [skills](https://developers.openai.com/codex/skills/).

## What to install

| Component | Needed for | Download and verification |
|---|---|---|
| AI coding agent | Reading the paper, following the skill, and running local tools. | Use an already configured agent with file and terminal access, such as [Codex](https://developers.openai.com/codex/). Discovery paths in this kit target Codex; other clients may require a different skill location or explicitly reading `SKILL.md`. |
| Git | Versioning this kit. | [Git](https://git-scm.com/downloads); `git --version`. |
| Node.js 22 or newer and npm | Running HyperFrames. This kit's initial environment profile uses Node 22. | [Node.js](https://nodejs.org/en/download); `node --version` and `npm --version`. |
| HyperFrames | Authoring, previewing, and rendering compositions. | Agent plugin **or** standalone CLI; see below. |
| FFmpeg and FFprobe | Trimming, cropping, inspecting, assembling, and exporting media. | [FFmpeg](https://ffmpeg.org/download.html); `ffmpeg -version` and `ffprobe -version`. |
| Chrome/Chromium compatible with HyperFrames | HTML previews, snapshots, and rendering. | Start with `hyperframes doctor` through your chosen installation; follow its runtime setup instructions. If a system browser is required, use [Chrome](https://www.google.com/chrome/) or your distribution's Chromium package. Confirm actual launch with `check`; an open browser alone is not enough. |
| Poppler (`pdftotext`) | Extracting text when the paper is a PDF. | The `poppler-utils` package on Ubuntu/Debian; `pdftotext -v`. Scanned PDFs may need OCR. |
| VoiceStudio | Optional; recommended for local agent-driven narration. | [Electron application](https://github.com/debpalash/VoiceStudio/releases) and the models selected in the app. See the voice section. |
| Video perception plugin | Optional; helps inspect recordings. | Install `claude-video-vision` through a catalog supported by your agent and check which tools are available. FFmpeg can also extract frames. |
| Python 3 | Optional; only when a project needs additional processing. | [Python](https://www.python.org/downloads/). This kit requires no Python packages. |

HyperFrames documents [Node.js 22+ and FFmpeg as requirements](https://github.com/heygen-com/hyperframes/blob/main/packages/cli/README.md). The standalone profile below pins **HyperFrames 0.8.177** to avoid silent version changes. This is not a claim that it is the latest release. Verify an update before changing the profile.

On Ubuntu/Debian, install the system utilities with:

```bash
sudo apt update
sudo apt install git ffmpeg poppler-utils
```

Install Node through its official distributor or a version manager. If you already use `nvm`, run from this kit's root:

```bash
nvm install
nvm use
node --version
npm --version
```

`.nvmrc` selects the Node 22 release line. Running `nvm install` assumes `nvm` itself is already installed; its [official installation instructions](https://github.com/nvm-sh/nvm#installing-and-updating) cover that separate step.

### HyperFrames: choose one installation

**Agent plugin:** install HyperFrames through a plugin manager supported by your agent and load its `hyperframes` entry skill. Use the launcher and version supplied by that installation. Do not run standalone skill-update commands against a plugin or copy another machine's cache directories.

**Standalone:** the following commands use an explicit version and may download that npm package. Run them from this kit's root:

```bash
mkdir -p work
npx --yes hyperframes@0.8.177 init work/my-video --non-interactive
mkdir -p work/my-video/input/recordings
cp .agents/skills/scene/assets/BRIEF.template.md work/my-video/BRIEF.md
```

Scaffolding may check or install external skills; inspect the chosen version's behavior. Do not install a second skill set when you already use the plugin. Inside `work/my-video`, follow the development loop for your chosen installation. For standalone:

```bash
cd work/my-video
npx --yes hyperframes@0.8.177 doctor
npx --yes hyperframes@0.8.177 preview --background
npx --yes hyperframes@0.8.177 preview --status
npx --yes hyperframes@0.8.177 check --json
```

After reviewing the preview, render and inspect the actual output. Consult `render --help` for the installed version's output options:

```bash
mkdir -p renders
npx --yes hyperframes@0.8.177 render -o renders/review-v01.mp4
ffprobe -v error -show_streams -show_format -of json renders/review-v01.mp4
```

Keep the preview available during review; stop it with `preview --stop` when finished. Prefer the [installed version's documentation and command help](https://github.com/heygen-com/hyperframes/blob/main/docs/packages/cli.mdx) over flags remembered from another release.

### Voice: VoiceStudio

1. Install and open the Electron application. Ordinary narration does not require building its source code.
2. Choose a speech engine and install its required model in the app. Transcription may need another model. GPU, memory, and disk requirements depend on that choice; there is no single hardware requirement for every voice.
3. Under **Integrations**, export the MCP configuration for your agent. The default address is `http://127.0.0.1:3900/mcp/`; respect the installation's actual port and authentication.
4. Check `check_health`, list voices and personalities, and generate a short sample before the full narration. Use the `voicestudio` skill for audio production; `voicestudio-maintainer` is for maintaining the application.
5. Save a consistent voice profile and its generation parameters in the local project. Use an original synthetic voice or an authorized reference.

If the audio skill is not already available, VoiceStudio documents this skill-installation command for supported agents. Choose `voicestudio` for production and inspect the installer's target options; do not replace a working plugin installation:

```bash
npx skills add debpalash/VoiceStudio
```

See the [application guide](https://github.com/debpalash/VoiceStudio#readme) and [MCP documentation](https://github.com/debpalash/VoiceStudio/blob/main/docs/mcp.md). APIs and tools evolve: discover the running version's contract. A model listed in a catalog is not proof its files are installed.

Do not assume `instruct` accepts free-form prose: some engines accept only enumerated attributes. List the available options. Prefer files or MCP resources for audio transfer instead of printing base64 into the conversation. Path-based inputs depend on the server's allowed directory; do not change that boundary to bypass a rejection.

## Make the next video

Clone or download this kit and open its root in your agent. The standalone shell commands above assume that starting directory.

1. Open this repository in your agent; it can discover `AGENTS.md` and the local skill. If you just installed the skill, start a new session to check discovery.
2. Create a project under `work/`, copy the brief, and specify the audience, objective, materials, language, duration, and anonymous or public release mode.
3. Keep real research materials inside the working project. Record the source of every metric and the usable windows of each recording.
4. Use the prompt below. The agent should adapt the script, duration, and edit to the supplied material, following the production guide.
5. Review visuals, numbers, and voice in the final MP4. Identify the approved file clearly.

```text
Use $scene to produce the video described in work/my-video/BRIEF.md.
Read the paper and inspect the supplied recordings before writing the script.
Explain the method with SVG illustrations and show the requested demonstrations and metrics.
Align narration to measured durations and follow the brief's visual direction.
Deliver the editable project, the MP4, and a record of the checks performed.
```

Adjustable starting style: 1920×1080 at 30 fps; black background; clear typography; SVG animation that explains the method; enough time to observe demonstrations; readable metrics; and English narration with measured delivery. A male voice is a starting preference, not a requirement for every paper.

There is no fixed one-minute limit. The time needed to explain and observe the experiments drives the script.

## Usage examples

These are generic prompts for a project in `work/my-video/`. Replace the filenames and source locations with the materials you supply. They describe a workflow, not an existing study; they contain no measured research values. Keep all project-specific input and output inside the ignored `work/` directory.

### 1. Create a complete research video

```text
Use $scene. Read work/my-video/input/paper.pdf and inspect the recordings in
work/my-video/input/recordings/. Use the brief as the source of project decisions.
Create an English research video with a black background and clear typography.
Explain the method with SVGs, then show the demonstrations and requested results.
Use enough time to observe the experiments instead of imposing a one-minute limit.
Draft the storyboard, generate a measured male voice sample, and follow the
installed HyperFrames workflow through review and export. Keep the work local.
```

### 2. Follow a visual reference

```text
Inspect work/my-video/input/reference-video.mp4 before proposing the visual style.
Borrow its pacing, typography hierarchy, and restrained academic bookends.
Use the supplied paper and recordings for the research content.
Follow the brief's release mode when deciding which identities may appear.
```

### 3. Improve the method illustrations

```text
Validate every method animation against the paper's equations and architecture.
Show each mechanism becoming active with a clear SVG state change.
Check block boundaries, arrows, reference markers, labels, and equation meaning.
Keep the already accepted footage and metrics scenes unchanged.
```

### 4. Select a better recording and integrate results

```text
Use only work/my-video/input/recordings/experiment-b.mp4 for the real experiment.
Remove the previous camera view and do not repeat the same flight or trial twice.
Show this recording for the first time beside its aggregate results panel.
Trim preparation and ending operations, including takeoff or landing if irrelevant.
If an image-plane trail helps, label it as a 2D annotation rather than ground truth.
```

### 5. Add a qualitative simulation view

```text
Use work/my-video/input/recordings/simulation-overview.mp4 as a visualization only.
Keep the outbound sequence through the checkpoint and exclude the return segment.
Crop the simulator and visualization windows to remove application and desktop chrome.
Keep synchronized views from the same frames. Do not add metrics to this chapter.
```

### 6. Add a quantitative simulation chapter before the real results

```text
Add work/my-video/input/recordings/simulation-benchmark.mp4 before the real-results scene.
Place its recording beside a metrics panel. Extract only the proposed method's
values from the benchmark table identified in the brief; omit baseline comparisons.
Preserve units, sample count, aggregation, uncertainty, and source locations.
Add English narration explaining what to observe and how to interpret these values.
Shift all following scenes, captions, narration, and the closing by the added duration.
```

### 7. Improve narration without rushing

```text
Review the exact export work/my-video/renders/review-v03.mp4 and measure its pauses.
Use the selected male voice with clearer articulation and more measured delivery.
Add useful information supported by the paper beyond what is written on screen.
Keep short observation pauses, but fill unintended long gaps, especially in demos.
Measure the new takes and regenerate or rephrase overruns instead of speeding them up.
Transcribe the numbers and listen to assess naturalness; report unavailable checks.
```

### 8. Prepare an anonymous review export

```text
Prepare an anonymous version for peer review.
Remove names, affiliations, institutional marks, identifying links, and credits
from active scenes, raster cards, captions, speech, visible desktop details, and metadata.
Keep the title and scientific explanation. Preserve the accepted method and footage.
Inspect the final MP4 and identify the submission file separately from earlier exports.
```

For further revisions, name the exact export and scene, describe the requested change, and say which accepted sections should remain. This gives the agent a concrete review target instead of an ambiguous instruction to edit the latest video.

### Use the skill in another repository

Copy the entire `.agents/skills/scene/` directory into the other project's `.agents/skills/`, preserving `references/`, `assets/`, and `agents/`. To make it available across repositories for one user, Codex also supports `~/.agents/skills/`. Check discovery paths against your version's official documentation.

You do not need to reinstall HyperFrames or VoiceStudio if they already work. This skill defines the editorial direction; those products' skills define their technical contracts.

## What belongs in a working project

Alongside the HyperFrames-generated files, maintain:

- `BRIEF.md`: video-specific decisions, including attribution or anonymity.
- `STORYBOARD.md`: scenes, durations, demonstration purposes, and metric placement.
- `CLAIMS.md`: claims and values, linked to their table, figure, page, or other source.
- `assets/`: local derivatives with their crops and provenance recorded.
- `voiceover/`: script, voice profile and parameters, takes, and measured alignment.
- `validation.md`: completed checks, failures, and limitations.
- The approved MP4, with an unambiguous filename.

## Issues to watch for

| Symptom | Response |
|---|---|
| Incompatible Node version | Check the executable in the agent's own terminal, activate the correct version, and verify again. |
| Chrome cannot start or a local port is denied | Record the actual error and fix the available runtime or permissions. Do not report a passing `check` when the browser was skipped. |
| Renderer unavailable | FFmpeg can trim, assemble, or replace audio on already rendered scenes. It does not render HTML/GSAP animation. Describe any alternative assembly accurately. |
| HTTP command fails but MCP responds | Use the connected MCP transport. One denied HTTP call does not establish that the application is unavailable. |
| Long unintended gaps in narration | Measure the intervals; add explanations supported by the paper or redistribute speech, preserving useful observation pauses. |
| Fast, artificial, or inconsistent voice | Review a sample, keep one profile, and rewrite or regenerate sections. A speed multiplier does not guarantee the same cadence across voices. |
| Transcript looks correct | Recognition checks content; it does not establish naturalness, pronunciation, or visual synchronization. Listen to the final audio. |

## Keep this kit shareable

`work/` is Git-ignored for production projects. Common paper, image, audio, and video formats, caches, and local configuration are also ignored. These exclusions help prevent accidental additions; they do not replace reviewing files before sharing a repository.

Version only generic instructions and templates. Before publishing, inspect `git status`, staged files, and history. This kit does not configure remotes or publish content automatically.

External references belong to their respective projects; their licenses and distribution requirements are independent of this kit.

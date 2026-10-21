---
name: scene
description: "Create or revise an academic research video from a paper and experiment recordings, combining method illustrations, traceable results, and narration. Use for research promos and supplementary videos; not for writing or reviewing the paper itself."
---

# SCENE

Scientific Communication through Explanation, Narration and Evidence.

Produce an editable video project and a clearly identified review export. Explain the contribution accurately and leave enough time to observe the evidence. Adapt to the supplied paper and recordings; do not copy a previous research project.

## Start from the brief

Read the current project's `BRIEF.md` and the [production guide](references/production.md). If no brief exists, copy the [brief template](assets/BRIEF.template.md) into the working project and fill it from the conversation and supplied files. Ask only for material decisions that cannot be inferred, such as missing sources or an unspecified release mode when identification matters.

For the kit repository, create article-specific projects under `work/`. When this skill is copied elsewhere, follow that repository's private working-directory convention instead. Keep research materials out of the shareable skill.

Initial preferences are black backgrounds, restrained typography, English narration, a measured male voice, and 1920×1080 at 30 fps. They are editable defaults. Existing user choices and a current design specification take precedence. Duration follows the evidence rather than a fixed one-minute limit.

## Use the installed production tools

- Load the `hyperframes` entry skill before composition work. Follow its installed version's authoring, history, preview, and render contracts. Use the existing plugin launcher when applicable; do not replace it with a standalone update.
- For HTML, use `hyperframes-core`; for explanatory animation, use the relevant animation guidance. Use `media-use` for media operations and provenance. The kit does not replace those technical skills.
- For VoiceStudio generation, use `voicestudio`, discover actual voices and model readiness, and keep one voice profile consistent. The maintainer skill is not an audio-production workflow.
- When video-perception tools are available, follow their inspection sequence. If unavailable, use local metadata and decoded frames, stating the coverage and any audio-analysis limitation.
- Do not add cloud processing, model downloads, publication, or a different generation provider without an applicable user choice. Reuse established authorization; do not repeatedly ask about already settled edits.

## Deliver the research story

1. Read the paper and inspect recordings before drafting claims. Build a small `CLAIMS.md` that ties each statement or number to its source and evaluation conditions.
2. Assign each scene a purpose: introduce the contribution, explain a mechanism, demonstrate behavior, or present evidence. Add only the scene types the material supports.
3. Write a timed `STORYBOARD.md`. When revising an accepted video, preserve unrelated scenes; propagate duration changes to subsequent footage, captions, and audio.
4. Explain the method with purposeful SVG states and transitions grounded in the paper. Check what is internal or external to each block, which signals activate a term, and what is an illustration versus measured data.
5. Edit recordings into intelligible observation windows. Remove irrelevant setup and desktop chrome; preserve aspect ratio and disclose speed changes. Present metrics beside a representative recording when useful, identifying the aggregation separately.
6. Generate an initial voice sample, then narration in coherent sections. Measure actual takes, adjust phrasing or scene time, and assemble without silently cutting or accelerating speech. Add useful explanation beyond the visible labels when supported by the paper.
7. Produce the correct public or anonymous bookends and inspect identification in the final media, not just the HTML.
8. Run the framework checks and review decoded export frames, transitions, metrics, timing, silence, and audio. Transcription is a content check, not listening. Report what could not be verified.

Use the production guide for the details of each stage. Do not create elaborate tooling when the installed CLI, media utilities, and a few local records suffice.

## Completion

Hand over the editable project, final MP4, narration script, source/evidence records, and `validation.md`. Name the actual duration and meaningful limitations. A passing lint check is not a passing browser render, and an export assembled from previously rendered scenes is not a new HTML render.

The final handoff should describe the result and link to the deliverable. It should not require the reader to reconstruct the outcome from progress messages.

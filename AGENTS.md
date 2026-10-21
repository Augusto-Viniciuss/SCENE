# Agent instructions

This repository contains a generic workflow for academic videos. Papers and experiment materials belong in local projects under `work/`, which is excluded from Git.

- To produce or edit an academic video, read `.agents/skills/scene/SKILL.md` and the project brief. When editing kit documentation, stay within the requested scope.
- Load the HyperFrames entry skill before changing a composition. Respect the existing installation: plugins and standalone installations use different execution and update mechanisms.
- Do not copy real research, measurements, images, names, identifiers, machine-specific paths, or project logs into this kit's shareable content.
- Use the brief template inside each project. Preserve original materials and create cropped derivatives without replacing the originals.
- Every scientific claim or metric needs a source. Distinguish aggregate results from the execution shown and conceptual illustrations from measured data.
- Producing a video does not authorize external sharing or publication. Prepare reviewable local artifacts and respect authorization already given.
- An approved change to one scene does not authorize rebuilding the others. Propagate duration changes to captions, narration, and the closing.
- After changing HTML, run the checks required by HyperFrames. Inspect the MP4 and report unavailable checks without treating skipped steps as passes.
- If `graphify-out/graph.json` exists, query the graph before searching code and update it after code changes. A documentation-only kit does not require creating a graph.

## Repository language

Keep instructions, skills, metadata, templates, and `README.md` in English. Only `README.pt-BR.md` is maintained in Portuguese. Keep its examples and shell commands aligned with the English README. This rule applies to repository content; conversation and video languages follow the user's instructions and project brief.

## Organization

`README.md` is the installation reference. The skill defines the editorial workflow, with details in its production guide. Avoid repeating the same procedures across multiple files.

To validate skill changes, use `quick_validate.py` from `skill-creator` when available and check relative links. Do not generate audio, render videos, or install models solely to validate a documentation change.

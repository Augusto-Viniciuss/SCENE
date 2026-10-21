# Production guide

Use this guide with the current brief and the installed tools' own instructions. It describes editorial decisions and checks, not a replacement media engine.

## Evidence before scripting

Read the supplied paper, especially the contribution, architecture, equations, evaluation protocol, and limitations. Extract PDF text locally when useful; inspect the page or figure if layout makes a table ambiguous.

In `CLAIMS.md`, record each proposed statement, source location, unit, aggregation, sample size, and conditions. Keep simulation and physical-experiment results separate. Distinguish complete-system timing from the timing of one component and identify percentiles correctly. Preserve uncertainty or sample deviation when relevant. Round only for spoken delivery while keeping the precise value in the evidence record.

Select only the requested methods and benchmarks. Do not import baseline results, percentages, or comparisons just because they appear in the paper. Never imply that an illustrative recording alone produced aggregate metrics. A recording's playback duration and a benchmark's mean task time can differ.

Describe the demonstrated behavior and the paper's actual guarantees. Do not turn a heuristic into a formal guarantee, a favorable experiment into universal performance, or an inferred trajectory into ground truth.

## Story and duration

A useful starting arc is title → method → demonstrations → results → closing. Some papers need neither a simulation chapter nor separate result chapters; select the structure from the evidence.

Give each scene an explanatory job. Keep bookends restrained and readable. Allocate the demonstration time before forcing the script into a target duration; a longer continuous experiment can be more informative than several short, disconnected shots. Avoid repeating the same footage unless the second presentation has a different, explicit purpose.

Record scene starts, durations, source in/out points, playback rates, metric context, and narration sections in the storyboard. When adding a chapter, update every subsequent start, the root duration, audio duration, captions, and any export assembly. Check frame boundaries when authored seconds are not multiples of the frame interval.

## Visual direction

Default to a black graphic background, light text, one or two functional accent colors, and consistent hierarchy. Use type sizes that remain readable in the intended delivery resolution. Preserve the supplied footage's color treatment unless an adjustment is requested or clearly justified.

Use SVGs to explain relationships, not as decoration. Establish the static diagram first, then animate the relevant mechanism: reveal an observation, draw a selected connection, activate a term, or show a state change. Reveal prerequisites before their consequences.

Validate the diagram against the paper:

- Block boundaries reflect the actual architecture.
- Inputs, outputs, labels, and arrows have the correct meaning and direction.
- Activation parameters affect the terms they actually control.
- Sampled references, predictions, observations, and executed trajectories are distinguished.
- Illustrative simplifications are labeled when they could be mistaken for data.

Inspect beginning, intermediate, and final states, including reverse seeking. Check labels against lines, arrowheads, markers, and equation baselines at full resolution. Avoid manual seeking or playback logic that conflicts with framework-owned media.

## Recording selection and cropping

Inspect metadata before extraction. With `claude-video-vision`, follow its required `video_info` → analysis when applicable → frame-inspection workflow. A connected plugin does not guarantee its transcription backend or models are ready. Report incomplete analysis or missing audio support.

Prefer a coherent recording that clearly shows the phenomenon. Remove irrelevant waiting, resets, setup, and ending operations when they do not support the message. Crop application title bars, taskbars, panels, cursor distractions, and personal information. Preserve the meaningful viewport and its aspect ratio.

For synchronized application views, take both crops from the same original frames. Add the gutter and labels in the composition. Check early, middle, and late crop samples against the original; camera motion can expose a border that was absent in one frame.

Keep originals intact. Record source path within the private project, file hash, source window, frame rate, crop coordinates, derived dimensions, and playback rate. Do not translate recording playback speed into a scientific speed claim.

If adding an estimated image-plane trail or another annotation, label what it is. Keep it aligned with the camera view, reset it at the chosen in-point, and do not present it as calibrated spatial measurement.

## Metrics beside demonstrations

Use a stable, readable results panel when the viewer should watch the experiment and read the numbers together. Show method, benchmark, sample count, aggregation, and units. Separate mean and uncertainty visually if a single long number is hard to read.

Keep the representative execution and full evaluation set distinct. Technical timing labels should state the component and percentile. Avoid animated counters for precise research measurements unless a clear explanatory reason justifies them.

If a chapter is only qualitative visualization, do not add metrics to it simply because another chapter has them. A requested quantitative chapter can follow a qualitative one without replacing it.

## Narration

Write speech for the listener rather than reading every on-screen label. Use shorter clauses, concrete explanations, and transitions between ideas. Extra information should explain why a mechanism matters, what the viewer should observe, or how to interpret a measurement; it must remain supported by the paper.

Start with a short sample of the requested voice and language. Keep the same saved profile across sections. Record the engine, profile, validated instruction attributes, speed, and quality settings. Do not assume profile IDs transfer to another machine.

Estimate an initial word budget with a measured research-speaking pace, then use actual generated durations. A starting estimate around 130–155 words per minute may help for English, but technical terms, pauses, and voice engines vary. A numeric speed multiplier is not a portable speaking-rate specification.

Generate coherent sections rather than isolated words or captions. If a take overruns, first rephrase, regenerate, or allocate more time. Do not silently time-stretch it to fit. If a scene has unintended empty space, add supported explanation or redistribute the section; leave deliberate observation pauses when they help.

Measure silence and review gaps of several seconds rather than deleting every breath. Check for overlap, clipping, truncation, abrupt edits, and unwanted original footage audio. Keep narration audible if there is a music bed. Music is optional, not an automatic fix for an incomplete script.

Transcribe final audio to catch omitted values, negations, and names. Listen to assess prosody, pronunciation, pacing, and naturalness. If the agent only has transcripts and signal analysis, say so; do not report having heard the result.

## Public or anonymous release

For a public video, use only the provided identities and assets. Preserve official institution names and supplied logo artwork.

For an anonymous review version, inspect all active scenes, text, images, captions, credits, spoken audio, visible application information, filenames shown on screen, and export metadata. Remove author identities, affiliations, institutional marks, personal paths, contact details, funding identifiers, and identifying project links as applicable. Do not merely remove a text row while leaving the same information in a raster card or closing logo.

Keep identified archives separate from the submission deliverable. Deliver the specific anonymous MP4; do not substitute an entire working folder containing source papers or earlier exports.

## Validation and fallback

Use the installed HyperFrames workflow to check HTML, preview, and render. After an HTML change, run its full check and fix actionable errors. Inspect scene midpoints and transitions, not just a single opening frame. Check deterministic seeking and the final scene's actual output duration.

Probe the final file for video/audio streams, resolution, frame rate, duration, and metadata. Decode representative frames around every changed section and verify the actual output, including the last frame. Use a frame-appropriate timing tolerance rather than exact equality between arbitrary authored seconds and frame counts.

When Chrome or local ports are unavailable, distinguish the specific browser failure from missing assets or invalid HTML. Do not keep retrying the same unavailable operation or describe skipped checks as successful.

FFmpeg can cut, crop, assemble, and mux rendered scenes. It cannot execute HTML animation. If approved rendered scenes already exist, an alternative assembly may combine those scenes with the exact new local static artwork and footage, provided the result and any differences are explained. New HTML animations still require a functioning render path; do not replace them with an unlabeled approximation.

In `validation.md`, state the checks actually performed, their results, skipped checks, the export path and duration, and any remaining question that requires listening or visual review. Preserve accepted scenes when they are outside the requested edit.

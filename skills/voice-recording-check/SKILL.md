---
name: voice-recording-check
description: "Use when a person's recorded voice for a video or podcast sounds off (warbly, robotic, AI-like, dull, pumping) or before building a video from their recording. The agent cannot listen, so this finds whether the damage is in the source file or in the processing using measurements as hints and short A/B clips of the same words for the person's ear to judge. Also covers processing rules that leave the voice untouched."
---

# Voice recording check

Needs: speech model

The agent cannot hear audio. Never claim a sound problem is fixed, or name its cause, from reasoning or measurements alone. Measure, then hand the person short A/B clips of the same words so their ear decides. Their ear outranks every measurement.

## 1. Measurements are hints, not a verdict

Run these on the upload before any processing, and report them as hints:

- **Format chain:** `ffprobe` codec, sample rate, bitrate. A file name suggesting an online editor or converter means at least two lossy encodes.
- **Frequency cutoff:** energy per band. A cliff, such as nothing above 17 kHz, means a lossy MP3 encode.
- **Silence floor:** share of 20 ms frames below -60 dB. A large share near -70 dB means noise suppression or gating ran before you got it (an editor's voice enhancer, OS mic enhancements, call-app noise suppression).
- **Spectrogram** of 5 s of speech: pure black between words and patchy mid and high bands.

All four can point at a damaged source while the untouched upload sounds fine to the person, with the real damage in the processing. Never conclude "the source is damaged" until they have heard the untouched clip.

- Valid: "Measurements hint at noise suppression in the upload, but I can't hear it. Here are 4 clips of the same words, upload vs final. Which one sounds off?"
- Invalid: "21% of frames sit at -70 dB, so your upload is damaged; send the original."

## 2. Processing rules: touch the voice as little as possible

- **Never stretch or squeeze the voice.** Time-stretch filters (`atempo`, `rubberband`) change how the person sounds. To slow a section, lengthen only the pauses between phrases: speech stays untouched, the section gets longer.
- **Keep the recording's own sample rate** end to end. Downsampling (for example to 24 kHz) makes the voice dull.
- **Loudness:** one fixed gain to about -16 LUFS, using two-pass `loudnorm` with `linear=true`. Never one-pass `loudnorm` inside the renderer, which pumps the level up and down.
- **Encode once at the end** (for example AAC 192k, 48 kHz). No MP3 in the middle.
- **Cuts:** 10 ms fades at each join. Accept a cut only when speech-to-text of the joined audio reads cleanly.

- Valid: "Slowed the intro by adding 300 ms to each pause; speech samples unchanged."
- Invalid: "Slowed the intro with atempo=0.9."

## 3. Let the person's ear decide

Before sending clips, null-test each processed clip against the untouched one: align them, subtract with the best gain, and measure what is left. If the leftover is below about -30 dB, the two are the same audio. Do not send them as separate versions. Say in one line that the step left that part unchanged, and send only the untouched clip plus any real candidate fix.

- Valid: "The editing step left this part identical to your upload, so I'm sending only the upload clip."
- Invalid: sending A, B and C clips when the null test showed B and C equal to A. The person hears identical clips and loses time.

Make 6 to 10 s clips of the same words: the untouched upload, and the final video's audio. One pair from an unaltered section, one from a slowed or cut section. Name each clip by what it is. Ask which one has the problem.

- **Untouched upload sounds fine:** the processing did it. Make a clip after each step to find which one, then remove that step or replace it with one that leaves the voice alone.
- **Untouched upload also sounds bad:** the source is damaged. Ask for the original recording from before any editor or enhancer. For next time: noise suppression off in the OS, call app and editor; export WAV or high-bitrate audio; send that file. A filter can soften the damage but not remove it, so offer softened clips only as a stopgap.

- Valid: "Clip 1 is your upload, clip 2 is the final. Same sentence. Which sounds off?"
- Invalid: "Fixed the audio: switched the slowdown method and kept the full sample rate." (nothing heard, no clips)

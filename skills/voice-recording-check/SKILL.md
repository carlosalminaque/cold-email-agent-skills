---
name: voice-recording-check
description: "Use before processing a person's recorded voice (changing its speed, cutting retakes, levelling it, building a video on it) and when a recording sounds wrong to them: warbly, robotic, AI-like, dull, pumping, odd after a speed-up. An agent has no ears, so it uses numbers as hints and same-words A/B clips for the person to judge. Covers a safe speed-change method, retake cuts, and checking lines spoken by an AI voice."
---

# Voice recording check

Needs: speech model

An agent has no ears. A statement that audio is fixed, or that a named thing caused the fault, cannot come from logic or numbers. Take the numbers, then give the person brief clips where the same words play in each version. What they hear beats anything you measured.

Read this before the first edit, not after a complaint.

## 1. Treat numbers as clues

On the raw upload, before you change anything, collect these and label them as clues:

- **Encode history:** codec, rate and bitrate from `ffprobe`. A name that points to a web converter or editor suggests two or more lossy passes.
- **Top end:** band energy. A hard wall (say around 17 kHz) points to MP3.
- **Quiet frames:** how many 20 ms frames fall under -60 dB. A big group around -70 dB points to a noise gate or suppressor upstream, such as an operating system mic option, a call app or an editor's voice tool.
- **Spectrogram:** five seconds of talk. Look for dead black gaps and blotchy upper bands.

Every clue can point the wrong way. A file can look damaged on all four and still sound fine, with the fault added later by processing. Hold any "bad source" verdict until the person has listened to the raw clip.

- Valid: "These numbers suggest suppression in your file, but I can't hear it. Here are four clips of one sentence, yours and the final. Which sounds wrong?"
- Invalid: "A fifth of your frames sit near -70 dB, so the upload is ruined. Send another."

## 2. Get word times before any cut

Run speech-to-text that returns word or token times, on chunks split at pauses. List phrases with their start and end before you pick a cut. Afterwards transcribe the joined result and read all of it.

## 3. Retakes

- "Sorry, let me repeat that" redoes what came just before it. Remove the failed try and that phrase; keep the redo.
- Several tries in a row: only the final one stays.
- A redo may begin before the failed line. Keep it from its own start and remove the older version of whatever it repeats.
- A redo can also straddle files: the tail of one upload may repeat a paragraph that the next upload starts over. Keep the complete version once and drop the other copy.
- If the speaker skipped or changed lines, what they said wins. Update the script and captions to match them.
- Place each cut on the quietest 10 ms of the gap, with 10 ms fades on both sides.
- When joining slides or sections, leave about a second of pause between them.

- Valid: "Three attempts at that sentence: kept the third, removed the first two and both apologies."
- Invalid: keeping the first attempt, or keeping a script line nobody said.

## 4. Processing: change as little as you can

- **Slowing a part down:** add length to the pauses only. Speech samples do not change.
- **Speeding a recording up, only when the person asks for it on that recording:** run ffmpeg `atempo` on the uncompressed edit (the WAV after cuts), never on compressed audio pulled from a finished video. `atempo` works in the time domain. Then confirm the median pitch of one passage moved by no more than about 2%.
- **Banned on speech:** `rubberband` and every other phase-vocoder stretch, whatever the quality flags.
- **Video after a speed-up:** retime the finished picture to the stretched audio instead of rendering again, so on-screen highlights stay on their words.
- **If the sped-up voice still sounds off to them:** do not argue for the method. Make audio-only options of equal length, null-test them against each other (section 5), and let them pick before any video is rebuilt.
- **Sample rate:** the recording's own, from start to finish. Going down to something like 24 kHz leaves speech dull.
- **Level:** a single fixed gain near -16 LUFS from two-pass `loudnorm` with `linear=true`, applied after any stretch. One-pass `loudnorm` in a renderer makes the level pump.
- **Encode:** one time, at the end (AAC 192k at 48 kHz is a fair default). Skip MP3 midway.

- Valid: "12% faster as you asked, `atempo` on the edit WAV; median pitch 142 Hz before, 143 Hz after; picture retimed, no re-render."
- Valid: "Intro slowed by adding 300 ms to each pause; speech samples unchanged."
- Invalid: "Used `rubberband` with formants preserved, so it's clean."
- Invalid: speeding up a video nobody asked to speed up.

## 5. The ear decides

Null-test first. Line up each processed clip with the raw one, subtract at the best gain, and measure the remainder. Under roughly -30 dB means no audible edit took place: do not offer them as two versions. Say that step changed nothing here and send the raw clip plus any real fix.

- Valid: "That step changed nothing in this part, so you only get the raw clip."
- Invalid: three clips that the null test showed are one clip. The person loses time on a difference that is not there.

Cut clips of 6 to 10 s with matching words: raw, and from the final. Take one pair where nothing was edited and one where something was slowed, sped up or cut. Label each by what it is, and ask which is wrong.

- **Raw is fine:** processing caused it. Export after each step to locate the step, then drop it or swap it.
- **Raw is bad too:** ask for the recording from before any editor or enhancer. Next time: suppression off everywhere, WAV or a high-bitrate export. Filters can only soften this, so offer them as a stopgap.

- Valid: "Clip 1 is yours, clip 2 is the final, same sentence. Which sounds off?"
- Invalid: "Fixed it by changing the method." (no clips, nothing heard)

## 6. Lines spoken by an AI voice

- Transcribe every generated line back and compare it with the script. Redo any line under about 0.9 match.
- Also redo any line whose transcript runs longer than the script, or repeats four or more words the script does not repeat. A clone can say a sentence twice and still score well.
- Clones can swallow a short first word. Reword the line to open with a longer phrase, and keep on-screen text the same as the audio.
- Whether a clone sounds like the person is for that person to say: play their real take and the clone on the same words. If it does not sound like them, ask for a few minutes of their normal speech as a fresh reference recording.
- One generation that holds several lines needs splitting afterwards. Silence detection fails here, because the gaps between lines are no longer than the gaps between sentences. Transcribe with word timestamps, align the words to the script, and cut midway between the last word of one line and the first word of the next.

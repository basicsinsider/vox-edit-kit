# Taiwan podcast — sound plan

The intro's `project/intro/music_cuesheet.json` uses a layered Melting Glass family, including Melting Glass instruments, Woodwind Reviere bass as a drone and Lightbulb Moment instruments/drums for a numbers pulse. These stems were fetched through the supplied Epidemic access and retimed for the podcast in `music_cuesheet.json`. Listening and editorial approval remain outstanding.

| Source seconds | Narrative | Direction |
|---|---|---|
| 0–17.600 | Tsao and the insight | Restrained texture and low pulse; leave space for both voices. |
| 17.600–48.080 | Telephone export growth and UMC profits | Build a light pulse through the 4 million / 24 million comparison; avoid an exaggerated sting on a conversational reaction. |
| 48.080–119.070 | Collapse, foundry idea and board permission | Thin the pulse as the market falls; return a measured analytical layer for the idea and board. |
| 119.070–192.330 | Condition, adviser and New York | Neutral forward motion, growing warmer on the return; do not imply the unnamed person's identity. |
| 192.330–260.200 | Questions and conversational explanation | Thin layers to protect dialogue and reactions; avoid masking short interjections. |
| 260.200–299.000 | Board reversal | Withdraw optimistic layer and introduce restrained tension, ending with the source sentence. |

After picture lock, use each composition's actual SFX markers with `tools/audio/place_sound.py`, then the manual's hierarchy/restraint pass. Sound the significant visual movement rather than every small object. Source audio is the sole dialogue track at unity: no processing, gain change or retiming. Build music and SFX under it, targeting about 14 LU below the voice, then run the short-window voice/music scan and mix measurements and listen to the loudest moments. The beds and final mix were built and measured. After the restraint pass, the SFX bed was attenuated by 8 dB. The music and music-plus-SFX scans found no 0.4 s or 3 s speech windows under the 12 LU separation threshold; the final output and source both measured −17.6 LUFS-I. The final mix has not had a human listening review.

Source-only measurement: FFmpeg EBU R128 integrated loudness −17.6 LUFS and loudness range 4.1 LU over the full source. This is analysis only; the source was not changed. The final bed must also be checked in local speech windows, not just against this average.

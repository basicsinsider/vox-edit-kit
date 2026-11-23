# 720p render helpers (Sonnet), launched 2026-11-22 06:36–06:39 UTC — one per segment, 720p pieces pushed to `render/<seg>`
cts01 session_017jFZyLkaZi2iEo1XbmWVTN · cts02 session_017jFZyMTCKo27qvfjwUpfC9 · cts03 session_017jFZyKApXbpkBnzcMLo7nf
cts04 session_017jFZyJbTKrhuZfxGRC6PWX · cts05 session_017jFZyNAWFRezKGHDt93bdQ · cts06 session_017jFZyNEhGnFRzdXezit8tw
cts07 session_017jFZyMsUKjCvhgbYd4boPK · cts08 session_017jFZyNi35FPeVu1NXNQEcD · cts09 session_017jFZyK1cdt3Enf4rjgtX1v
cts10 session_017jFZyLddbnvYEDxpftkkTz · cts11 session_017jFZyLyoJFJTmofJ6utzx8 · cts12 session_017jFZyK3RXGCiA3tzCmfznn
cts13 session_017jFZyLYX1u124RBuQwKs4w · cts14 session_017jFZyMqDeBAXh7XrJTp5xg
Command on each: `SCALE=720 tools/render_piece.sh ct 1341.912 <seg>` (project/cartels/HELPER_PROMPT.md).

# Final 4K helpers (2026-11-23 00:06 UTC, HELPER4K2_PROMPT.md, CRF 20 medium, parts pushed to render4k/<seg>)
cts01 session_017jFZyLMvnxk9PpVxABuYgX · cts02 session_017jFZyM7YtCSwq5yVX1KAN4 (+ backup (b) session_017jFZyMchppT2UiJ1GZNxqx) ·
cts03 session_017jFZyJHrf7LfjbtoLzvYVK · cts04 session_017jFZyLVyV8NfbxY4VB4zEM · cts05 session_017jFZyLUwiEx3zYFiswQScm ·
cts06 session_017jFZyLBkMg64Yi6u3eYjf5 · cts07 session_017jFZyMxtW2d1Rouv9VfFqf (refused to push on a lead message → (b) session_017jFZyNVAAbAxPkmWWctRZE
with the push in its own prompt) · cts08 session_017jFZyJe9Jxxzs9KzsR9MUd · cts09 session_017jFZyNQojV29gkaBEiJdSt · cts10 session_017jFZyKDi9wxwScFi66YNAF ·
cts11 session_017jFZyN5fJauqP1cTRLGZND · cts12 session_017jFZyMNLP4vtUZV9ciLM2g · cts13 session_017jFZyLR6J2YAL9gZnYN8h9 · cts14 session_017jFZyNR8afXbBC4TVpA3sa
Lesson: put the hand-off (push) step in the helper's FIRST prompt — a later message from the lead is treated as a peer request and may be refused.

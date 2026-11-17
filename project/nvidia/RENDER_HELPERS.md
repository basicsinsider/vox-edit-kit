# 1080p render helpers (Sonnet), launched 2026-11-17 05:00–05:10 UTC — one per segment, pieces pushed to `render/<seg>`
nvs01 session_017jFZyJUJDDgVkD2QLzM6PN · nvs02 session_017jFZyKj12RfhsvR7fk3u6q · nvs03 session_017jFZyMCsN815LU2gjAgoPw
nvs04 session_017jFZyMHEnJxq4NEdEeRoMe · nvs05 session_017jFZyKbkDSgwYho5xd6ph3 · nvs06 session_017jFZyMX5yitePWQJwDgPSq
nvs07 session_017jFZyJRFubDqiUaaiQkVWF · nvs08 session_017jFZyMZR8LDyYJAQMXXusK · nvs09 session_017jFZyNsT7jh4Me4diaSXra
nvs10 session_017jFZyNZoyF5oMmYbfyZkHv · nvs11 session_017jFZyNERQMpV6V97gCwqpZ · nvs12 session_017jFZyLoQxyjcwG3voMsV2Y
nvs13 session_017jFZyJNXwptvX29gB4z7GL · nvs14 session_017jFZyLpQVsTbViECeVAEwz · nvs15 session_017jFZyKpb8WwsxDv9fGiked
nvs16 session_017jFZyJ9ZatxA3PD5ay9iq7 · nvs17 session_017jFZyMwo2AmaFSXuyov6q8 · nvs18 session_017jFZyJbUZSHQy5o84TiBKQ
nvs19 session_017jFZyLYzoF7XRrmx1zRF1X · nvs20 session_017jFZyMmsEbmHssWyLXNp6Z · nvs21 session_017jFZyLN3jM3b3JPE4Enjy4
nvs22 session_017jFZyLjy7BQhZwzNBs9jP4 · nvs23 session_017jFZyNhZ3Tm6nseg634Tjj
Lesson: a create_session with `outcome_branch` starts that branch from the repo DEFAULT branch — the helper must
`git fetch origin claude/nvidia-edit && git checkout -B render/<seg> FETCH_HEAD` first (HELPER_PROMPT step 0). sparse_checkout_paths had no effect.

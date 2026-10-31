#!/bin/bash
# Starts tools/render_chunk.sh fully detached (survives the tool shell; never use a capped background tool call for renders).
#   tools/render_launch.sh c2 597.86 c4 601.44 ...   → progress: tail renders/render_log.txt
R="$(cd "$(dirname "$0")/.." && pwd)"
setsid nohup "$R/tools/render_chunk.sh" "$@" >> "$R/renders/render_queue.out" 2>&1 < /dev/null &
echo "launched: $*  (log: renders/render_log.txt)"

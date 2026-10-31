#!/bin/zsh
# usage: snap_c4s02.sh name t1,t2,... (LOCAL c4 seconds) — rebuilds compositions/c4s02.html, snapshots in work/c4s02
cd /home/user/vox-edit-kit && python3 project/c4/gen/build_c4s02.py >/dev/null && cd work/c4s02 || exit 1
at=$(python3 -c "import sys;print(','.join(str(round(float(x)-199.14,3)) for x in sys.argv[1].split(',')))" $2)
rm -rf .snap/$1; npx --yes hyperframes@0.8.217 snapshot --at $at --no-end -o .snap/$1 >/dev/null 2>&1; ls .snap/$1 | wc -l

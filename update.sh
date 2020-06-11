#!/bin/sh

set -e -x

git fetch upstream
git rebase upstream/master
cd python3
python -c 'from rename import *; rename_crimea()'
python check.py
NERR=$?
if test "$NERR" != "5" ; then
  echo "New errors have appeared."
  exit
fi
python -c 'from covid19ru.access import *; ru_timeline_dump()'
python plot.py

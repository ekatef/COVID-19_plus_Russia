#!/bin/sh

set -e -x

git fetch upstream
git rebase upstream/master
cd python3
python -c 'from rename import *; rename_crimea()'
python check.py
NERR=$?
if test "$NERR" != "6" ; then
  echo "New errors have appeared. Check the list above."
  exit
fi
python dump.py
python plot.py

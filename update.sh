#!/bin/sh

set -e -x

git fetch upstream
git rebase upstream/master

(
cd python3
python -c 'from rename import *; rename_crimea()'

  (
    set +e
    python check.py
    NERR=$?
    if test "$NERR" != "6" ; then
      echo "New errors have appeared. Check the list above."
      exit
    fi
  )

python dump.py
python plot.py
)


git add csse_covid_19_data/csse_covid_19_daily_reports/*csv
git commit -m 'Update daily data'

git add csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_RU.csv
git add csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_RU.csv
git commit -m 'Update timelines'

git add python3/*.png
git commit -m 'Update plots'

git push -f origin master

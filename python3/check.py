#!/usr/bin/env python

from covid19ru.check import check_all

err=check_all()
if len(err)>0:
  print(err)

exit(len(err))

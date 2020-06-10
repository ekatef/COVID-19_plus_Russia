#!/usr/bin/env python

from os import walk
from os.path import abspath, join
from covid19ru.defs import REGIONS, COVID19RU_ROOT



def rename(root:str=COVID19RU_ROOT, force:bool=False)->None:
  for root, dirs, filenames in walk(abspath(root), topdown=True):
    for filename in sorted(filenames):
      if filename.endswith('csv'):
        with open(join(root,filename), 'rb') as f:
          s=f.read()
        for en,_,en2 in REGIONS:
          s=s.replace(en.encode(),en2.encode())
        with open(join(root,filename), 'wb') as f:
          f.write(s)
  return


def rename_crimea(root:str=COVID19RU_ROOT, force:bool=False):
  for root, dirs, filenames in walk(abspath(root), topdown=True):
    for filename in sorted(filenames):
      if filename.endswith('csv'):
        with open(join(root,filename), 'rb') as f:
          s=f.read()
        s=s.replace("Sevastopol*,Ukraine".encode(),"Sevastopol,Russia".encode())
        s=s.replace("\"Sevastopol*, Ukraine\"".encode(),"\"Sevastopol, Russia\"".encode())
        s=s.replace("Crimea Republic*,Ukraine".encode(),"Republic of Crimea ,Russia".encode())
        s=s.replace("\"Crimea Republic*, Ukraine\"".encode(),"\"Republic of Crimea, Russia\"".encode())
        with open(join(root,filename), 'wb') as f:
          f.write(s)

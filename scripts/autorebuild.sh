#!/usr/bin/env bash

if ! [ -d "venv" ] ; then
  rm -rf venv
  virtualenv venv
  venv/bin/pip install -r requirements.txt
fi

if ! venv/bin/python scripts/reflist.py ; then
    echo -ne '\007'
fi

if ! rubber -d notes.tex ; then
    echo -ne '\007'
fi

inotifywait notes.tex references.bib chapters includes/*.tex chapters/*.tex $0
exec $0

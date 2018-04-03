#!/usr/bin/env bash

if ! [ -d "venv" ] ; then
  rm -rf venv
  virtualenv venv
  venv/bin/pip install -r requirements.txt
fi

if ! venv/bin/python scripts/reflist.py ; then
    echo -ne '\007'
fi

FILES="notes.tex literature.tex"

for f in $FILES; do
  if ! rubber -d "$f" ; then
      echo -ne '\007'
  fi
done

inotifywait $FILES references.bib chapters includes/*.tex chapters/*.tex $0
exec $0

#!/usr/bin/env bash

if ! python scripts/reflist.py ; then
    echo -ne '\007'
fi

if ! rubber -d notes.tex ; then
    echo -ne '\007'
fi

inotifywait notes.tex references.bib chapters includes/*.tex chapters/*.tex $0
exec $0

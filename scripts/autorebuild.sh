#!/usr/bin/env bash

rubber -d notes.tex
inotifywait notes.tex references.bib chapters chapters/*.tex $0
exec $0

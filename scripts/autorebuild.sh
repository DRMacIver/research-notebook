#!/usr/bin/env bash

rubber -d notes.tex
inotifywait notes.tex references.bib $0
exec $0

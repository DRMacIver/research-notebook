#!/usr/bin/env bash

rubber -d notes.tex
inotifywait notes.tex references.bib autorebuild.sh
exec $0

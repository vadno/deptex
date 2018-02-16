#!/usr/bin/env bash

python3 deptex.py test_magyarlanc.txt test_deptex.tex
pdflatex test_deptex.tex
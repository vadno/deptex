# deptex

**deptex** is an easy-to-use tool for generating latex sources of dependency graphs from the output of the dependency parser module of magyarlanc, a toolkit for linguistic processing of Hungarian.

The script can be run by this command: `python3 deptex.py arg1 arg2`

## arg1: input

**deptex** processes the output of the dependency parser module of magyarlanc. The output has the following structure: one line corresponds to one token and sentences are separated by an empty line. Every row consists of seven columns:

1. the identifier of the word within the sentence
1. wordform
1. lemma
1. POS-tag
1. morphological features
1. the identifier of the parent node
1. the dependency label

You can download **magyarlanc** from [here](http://www.inf.u-szeged.hu/rgai/magyarlanc). Please cite this article:

Zsibrita, János; Vincze, Veronika; Farkas, Richárd 2013: magyarlanc: A Toolkit for Morphological and Dependency Parsing of Hungarian. In: Proceedings of RANLP 2013, pp. 763-771.

```
@inproceedings{magyarlanc,
author = {Zsibrita, J\'{a}nos and Vincze, Veronika and Farkas, Rich\'{a}rd},
title = {magyarlanc: A Toolkit for Morphological and Dependency Parsing of Hungarian},
booktitle = {Proceedings of RANLP 2013},
pages = {763--771},
year = {2013}
}
```

## arg2: output

The output is a simple .tex file containing the minimal preamble. Every sentences parsed by magyarlanc gets an own dependency environment with the generated text and edges.

## dependencies

* Python3
* a TEX distribution, eg. TeXLive
* [tikz-dependency](https://ctan.org/pkg/tikz-dependency) package

## test

A sample file (test_magyarlanc.txt) is provided with two sentences parsed by magyarlanc. In deptex.sh the two steps (running deptex.py and compiling the pdf) are concatenated. In the .sh script run with the sample input file.

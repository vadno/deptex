#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    author: Noémi Vadász
    last update: 2018.02.16.

    dependency graph drawer
    input: output of magyarlanc dependency parser (http://www.inf.u-szeged.hu/rgai/magyarlanc)
    sentence delimiter  \n\n
    word delimiter     \n
    cells:
        index
        token
        lemma
        POS
        morphological features (detailes here: http://rgai.inf.u-szeged.hu/project/nlp/research/msdkr/univmorph.html)
        index of dependent
        type of dependency
    output: .tex file (using tikz dependency package)
"""

import sys


def read_magyarlanc():
    """
    reads output of magyarlanc
    :return: list of sentences that are lists of words
    """

    with open(sys.argv[1]) as inp:

        sents = inp.read().strip().split('\n\n')

    sentlist = []

    # needs extension to other punct marks
    punct = (':', '(', ')', '[', ']',
             '&', '%', '$', '#', '_', '{', '}', '~', '^', '\\')

    for sent in sents:

        wordlist = list()
        # empty note for ROOT
        wordlist.append(['0', 'ROOT', 'ROOT', 'ROOT', '', '', None])
        for word in sent.split('\n'):
            splitted_word = word.split('\t')
            if splitted_word[1] == '&':
                splitted_word[1] = 'and'
            elif splitted_word[1] in punct:
                splitted_word[1] = 'PUNCT'
            wordlist.append(splitted_word)

        sentlist.append(wordlist)

    return sentlist


def to_tex(sentlist):
    """
    arranges the output of magyarlanc according to tikz-dependency
    :param sentlist: list of sentences read from the output of magyarlanc
    :return: None
    """

    with open(sys.argv[2], 'w') as of:
        print('\\documentclass{minimal}\n',
              '\\usepackage[utf8]{inputenc}',
              '\\usepackage{tikz-dependency}\n',
              '\\begin{document}\n', sep='\n', end='\n\n', file=of)

        for sent in sentlist:
            print('\\begin{dependency}',
                  '\\begin{deptext}', sep='\n', end='\n', file=of)

            print(' \\& '.join([word[1] for word in sent]), end=' \\\\\n', file=of)
            print(' \\& '.join([word[3] for word in sent]), end=' \\\\\n\\end{deptext}\n', file=of)
            for word in sent:
                if word[6] is not None:
                    # None if it is empty ROOT node
                    print('\\depedge{', int(word[5]) + 1, '}',
                          '{', int(word[0]) + 1, '}',
                          '{', word[6], '}',
                          sep='', file=of)

            print('\\end{dependency}', sep='\n', end='\n\n\n', file=of)

        print('\\end{document}', file=of)


def main():
    sentlist = read_magyarlanc()
    to_tex(sentlist)


if __name__ == "__main__":
    main()

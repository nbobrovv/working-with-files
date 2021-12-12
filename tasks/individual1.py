#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает из текстового файла
три предложения и выводит их в обратном порядке.
"""


if __name__ == "__main__":
    with open("individual1.txt", "r", encoding="utf-8") as fileptr:
        sentences = fileptr.read()
        reverse_sentences = (sentences.splitlines())
        print(*reversed(reverse_sentences), sep='\n')

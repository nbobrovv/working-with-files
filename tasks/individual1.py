#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает из текстового файла
три предложения и выводит их в обратном порядке.
"""

if __name__ == "__main__":
    with open("individual1.txt", "r") as fileptr:
        sentences = fileptr.readlines()
        print(sentences)
        print()
        reverse_sentences = f"\n".join(reversed(sentences))
        print(reverse_sentences)
#!/usr/bin/python

badWords = open('../media/badWords.txt', 'r')
curseWords = badWords.read()
badWords.close()

greetings = open('../media/greetings.txt', 'r')
greets = greetings.read()
greetings.close()

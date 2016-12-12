#!/usr/bin/python
import wikipedia

searchItem = raw_input("What are you curious about today?\n->")
info = wikipedia.summary(searchItem, sentences=2)

print info

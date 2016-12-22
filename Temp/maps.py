#!/usr/bin/python3

import os
from os import *

print("Enter name of place")
a = input('->')
os.system ("google-chrome http://www.google.com/maps/place/" + a + '/')
pass
print('')

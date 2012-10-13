#!/usr/bin/env python

#	Project 3 - Netflix
#	Brett Canino
#	Instructor - Glenn Downing
#	Cs 373

# -------
#	To run the program
#		% python RunNetflix.py < Netflix.in > Netflix.out
#		% chmod ugo+x RunNetflix.py
#		% Netflix.py < RunNetflix.in > Netflix.out

#	To document the program
#		% pydoc -w Netflix
# -------

# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----	

netflix_solve(sys.stdin, sys.stdout)
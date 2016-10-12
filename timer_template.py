#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# timer_template.py: simple Python script for generating an analogue clock timer template
#                    given two circle diameters and the number of hours on the dial
#
# Copyright (C) 2016  Matthias Kolja Miehl
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
DESCRIPTION: simple Python script for generating an analogue clock timer template
             given two circle diameters and the number of hours on the dial
TASK       : simplify the creation of a geometrically accurate timer design
UPDATES    : https://github.com/makomi/timer_template
"""


# ------------------------------------------------------------------------------
# modules
import Tkinter as tk
from sympy import *
from math import *

# ------------------------------------------------------------------------------
# settings
d1 = 400       # diameter of day  circle [px]
d2 = 20        # diameter of hour circles [px]
n2 = 24        # number   of hour circles
padding = 1

# ------------------------------------------------------------------------------
# geometry
r1 = d1/2
r2 = d2/2

# image
imgHeight = imgWidth = 2*(r1+r2) + 2*padding
imgCenterX = imgWidth/2
imgCenterY = imgHeight/2

# hour circle angles
angle = range(0, 360, 360/n2)

# ------------------------------------------------------------------------------
# canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=imgWidth, height=imgHeight, borderwidth=0, highlightthickness=0, bg="white")
canvas.grid()

# ------------------------------------------------------------------------------
# monkey patch 'create_circle' to the Tkinter class 'Canvas'

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

# ------------------------------------------------------------------------------
# day circle
canvas.create_circle(imgCenterX, imgCenterY, r1, outline="black", width=1)
canvas.create_circle(imgCenterX, imgCenterY,  0, outline="black", width=1)

# hour circles
for i in range(len(angle)):
    x = int(imgCenterX + r1*cos(radians(angle[i])))
    y = int(imgCenterY + r1*sin(radians(angle[i])))
    canvas.create_circle(x, y, r2, outline="black", width=1)

# half-hour lines
#canvas.create_line(x-r2, y, x+r2, y, width=1)

# ------------------------------------------------------------------------------
# save canvas as postscript document
canvas.update()
canvas.postscript(file="timer_template.ps", colormode='color')

# ------------------------------------------------------------------------------
# window
root.wm_title("timer template")
root.mainloop()


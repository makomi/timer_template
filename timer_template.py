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
d1 = 210         # diameter of main circle  [px]
d2 = 10          # diameter of hour circles [px]
n2 = 24          # number   of hour circles
imgScaling = 2   # use a large integer scaling factor, to position elements with high accuracy
imgPadding = 1   # additional image border padding [px]

# ------------------------------------------------------------------------------
# geometry
d1 *= imgScaling
d2 *= imgScaling
r1 = d1/2
r2 = d2/2
angleFullCircle = 2*pi

# image
imgHeight = imgWidth = 2*(r1+r2) + 2*imgPadding
imgCenterX = imgWidth/2
imgCenterY = imgHeight/2

# hour circle angles
angleCirclesSector = angleFullCircle/n2
angleCircles = []
for i in range(n2):
    angleCircles.append(i*angleCirclesSector)

# half-hour line angle offset
angleLinesOffset = (angleCircles[0]+angleCircles[1])/2

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
canvas.create_circle(imgCenterX, imgCenterY,  1, outline="black", width=1)

# hour circles
for i in range(len(angleCircles)):
    x = int(imgCenterX + r1*cos(angleCircles[i]))
    y = int(imgCenterY + r1*sin(angleCircles[i]))
    canvas.create_circle(x, y, r2, outline="black", width=1)

# hour lines
for i in range(len(angleCircles)):
    x1 = int(imgCenterX + (r1-r2)*cos(angleCircles[i]))
    y1 = int(imgCenterY + (r1-r2)*sin(angleCircles[i]))
    x2 = int(imgCenterX + (r1+r2)*cos(angleCircles[i]))
    y2 = int(imgCenterY + (r1+r2)*sin(angleCircles[i]))
    canvas.create_line(x1, y1, x2, y2, width=1)

# half-hour lines
for i in range(len(angleCircles)):
    x1 = int(imgCenterX + (r1-r2)*cos(angleCircles[i]+angleLinesOffset))
    y1 = int(imgCenterY + (r1-r2)*sin(angleCircles[i]+angleLinesOffset))
    x2 = int(imgCenterX + (r1+r2)*cos(angleCircles[i]+angleLinesOffset))
    y2 = int(imgCenterY + (r1+r2)*sin(angleCircles[i]+angleLinesOffset))
    canvas.create_line(x1, y1, x2, y2, width=1)

# ------------------------------------------------------------------------------
# save canvas as postscript document
canvas.update()
canvas.postscript(file="timer_template.ps", colormode='color')

# ------------------------------------------------------------------------------
# window
root.wm_title("timer template")
root.mainloop()


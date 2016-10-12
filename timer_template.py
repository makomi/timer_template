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
import Tkinter as tk

# ------------------------------------------------------------------------------
imgWidth = 400
imgHeight = 400

d1 = 200               # diameter of day circle

# ------------------------------------------------------------------------------
root = tk.Tk()
canvas = tk.Canvas(root, width=imgWidth, height=imgHeight, borderwidth=0, highlightthickness=0, bg="white")
canvas.grid()

# ------------------------------------------------------------------------------
# monkey patch 'create_circle' to the Tkinter class 'Canvas'

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

# ------------------------------------------------------------------------------
imgCenterX = imgWidth/2
imgCenterY = imgHeight/2

# ------------------------------------------------------------------------------
canvas.create_circle(imgCenterX, imgCenterY, d1, outline="black", width=1)
canvas.create_text(imgCenterX, imgCenterY, text='.')

# ------------------------------------------------------------------------------
root.wm_title("timer template")
root.mainloop()


#!/usr/bin/env python3
""" MIDI Keyboard as a computer keyboard, where fast-presses generate upper
case letters.

Proof of concept.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Christoph Siedentop"
__copyright__ = "Copyright 2020, Christoph Siedentop"
__date__ = "2020-08-16"
__license__ = "GPLv3"

import mido
from pynput.keyboard import Key, Controller
from contextlib import nullcontext

inputs = mido.get_input_names()
inport = mido.open_input(inputs[1])
keyboard = Controller()

DICT = {
    45: "a",
    47: "b",
    48: "c",
    50: "d",
    52: "e",
    53: "f",
    55: "g",
    57: "h",
    59: "i",
    60: "j",
    62: "k",
    64: "l",
    65: "m",
    67: "n",
    69: "o",
    71: "p",
    72: "q",
    74: "r",
    76: "s",
    77: "t",
    79: "u",
    80: "v",
    81: "w",
    82: "x",
    83: "y",
    84: "z",
    39: Key.enter,
    38: Key.backspace,
    36: " ",
    54: ".",
    56: ",",
    58: "!",
}


def note2char(note):
    return DICT.get(note, "?")


while True:
    msg = inport.receive()
    if msg.type == "note_on":
        char = note2char(msg.note)
        # Type upper case letters (i.e. hold down Shift) if velocity is high.
        if msg.velocity > 70:
            modifier_context = keyboard.pressed(Key.shift)
        else:
            modifier_context = nullcontext()
        with modifier_context:
            keyboard.press(char)
            keyboard.release(char)

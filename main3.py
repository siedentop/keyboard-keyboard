#!/usr/bin/env python3
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
    66: "m",
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
        if msg.velocity > 70:
            modifier_context = keyboard.pressed(Key.shift)
        else:
            modifier_context = nullcontext()
        with modifier_context:
            keyboard.press(char)
            keyboard.release(char)

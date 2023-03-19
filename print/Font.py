"""
This is a short Font module i myself developed it to change
and access text colors as simple as possible

* It contains 3 list : Color Background Style
* RESET to reset your applied options

Usage : 
>>>> from Font import *
>>>> print(f " {Color['Red']} this is a Red text")

or

>>>> from Font import Background as bk
>>>> print(bk['Yellow'] + "this is a Red text")
"""

from random import randint

RESET = '\033[0m'

Color = {
    'Red': '\033[31m',
    'Green': '\033[32m',
    'Yellow': '\033[33m',
    'Blue': '\033[34m',
    'Purple': '\033[35m',
    'Cyan': '\033[36m',
    'Light Grey': '\033[37m',
    'Black': '\033[30m',
    'Dark Grey': '\033[90m',
    'Bright Red': '\033[91m',
    'Bright Green': '\033[92m',
    'Bright Yellow': '\033[93m',
    'Bright Blue': '\033[94m',
    'Bright Purple': '\033[95m',
    'Light Blueish-Cyan': '\033[96m',
    'White': '\033[97m',
}

Background = {
    'Black': '\033[40m',
    'Red': '\033[41m',
    'Green': '\033[42m',
    'Yellow': '\033[43m',
    'Blue': '\033[44m',
    'Purple': '\033[45m',
    'Cyan': '\033[46m',
    'Light Grey': '\033[47m',
    'Dark Grey': '\033[100m',
    'Bright Red': '\033[101m',
    'Bright Green': '\033[102m',
    'Bright Yellow': '\033[103m',
    'Bright Blue': '\033[104m',
    'Bright Purple': '\033[105m',
    'Blueish-Cyan': '\033[106m',
    'White': '\033[107m',
}

Style = {
    'Bold': '\033[1m',
    'Dim/Faint': '\033[2m',
    'Italic': '\033[3m',
    'Underline': '\033[4m',
    'Strikethrough': '\033[9m',
    'Not italic': '\033[23m',
    'Not underline': '\033[24m',
    'Not strikethrough': '\033[29m',
}


def Random_color() -> str:
    """
    Return code colors.
    Colors range from 0 to 263
    """
    color_code = f"\033[38;5;{randint(0,263)}m"

    return color_code

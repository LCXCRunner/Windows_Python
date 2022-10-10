from os import close
from guizero import App, Box, Text, PushButton
import time
import os
import sys

# Action you would like to perform
def counter():
    text.value = int(text.value) + 1

app = App("Hello world")
text = Text(app, text="1")
text.repeat(1000, counter)  # Schedule call to counter() every 1000ms

box_2 = Box(app, align="right")
Button = PushButton(box_2, text="Close Window", command=sys.exit)

app.display()
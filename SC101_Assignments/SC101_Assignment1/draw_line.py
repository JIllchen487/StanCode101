"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

cnt = 0
window = GWindow()
SIZE = 10
start_x = 0
start_y = 0
dot = GOval(SIZE, SIZE, x=0, y=0)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(action)

def action(mouse):
    global cnt
    global start_x
    global start_y
    global dot
    cnt += 1
    if cnt % 2 == 1:
        window.add(dot, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        start_x = mouse.x
        start_y = mouse.y
    else:
        line = GLine(start_x, start_y, mouse.x, mouse.y)
        window.add(line)
        window.remove(dot)


if __name__ == "__main__":
    main()

"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
time = 0

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
window.add(ball, x=START_X, y=START_Y)

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bounce)

def bounce(mouse):
    speed = 0
    global time
    if time < 3:
        ball.move(VX, speed)
        while True:
            if ball.x >= window.width:
                window.add(ball, x=START_X, y=START_Y)
                time += 1
                break
            else:
                speed = speed + GRAVITY
                ball.move(VX, speed)
                pause(DELAY)  # 太快人眼跟不上
                if ball.y >= window.height:
                    speed = -speed


if __name__ == "__main__":
    main()

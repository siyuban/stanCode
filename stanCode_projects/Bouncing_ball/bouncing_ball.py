"""
File: bouncing_ball.py
Name: 萬思妤
-------------------------
TODO:Create a bouncing ball at (START_X, START_Y) that has VX as x velocity and 0 as y velocity. Each bounce reduces
     y velocity to REDUCE of itself.
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

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.filled_color = "black"
    window.add(ball, START_X, START_Y)
    onmouseclicked(function)


def function(m):
    global count
    vy = 0
    if ball.y == START_Y and count <= 2:
        # limitation: Only when the ball is at the start point and the dropping cycle is  less than 3 times can
        # stimulate the ball to move by clicking the mouse.
        count += 1
        while True:
            if ball.y+ball.height < window.height:
                # When the ball reach the floor.
                ball.move(VX, vy)
                vy += GRAVITY
            else:
                vy = -vy*REDUCE
                vy += GRAVITY
                ball.move(VX, vy)
                if ball.x+ball.width > window.width or ball.y+ball.height > window.height:
                    # when the ball is out of window.
                    break
            pause(DELAY)
        ball.x = START_X
        ball.y = START_Y
        # Put the ball back to the start point.


if __name__ == "__main__":
    main()

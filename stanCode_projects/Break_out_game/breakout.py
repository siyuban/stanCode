"""
File : breakout.py
Name : 萬思妤
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

Breakout game using Class BreakoutGraphics.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000/50 # 120 frames per second.
NUM_LIVES = 3


def main():
    lives = NUM_LIVES
    graphics = BreakoutGraphics()
    # Add animation loop here!
    vx = graphics.get_velocity_x()
    vy = graphics.get_velocity_y()
    while True:
        graphics.ball.move(vx, vy)
        graphics.check_object()
        # when the ball hits the wall, it will bounce.
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.bounce_x()
        if graphics.ball.y <= 0:
            graphics.bounce_y()
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            graphics.rest_ball()
            if lives == 0:
                break
        vx = graphics.get_velocity_x()
        vy = graphics.get_velocity_y()
        # All the bricks are removed.
        if graphics.total_brick == 0:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

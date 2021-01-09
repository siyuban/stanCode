"""
File : breakoutgraphics.py
Name : 萬思妤
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

All the objects in class BreakoutGraphics.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle_width = paddle_width
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-PADDLE_OFFSET)
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball_radius = ball_radius
        self.ball.filled = True
        self.ball.fill_color = 'black'
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        # Initialize our mouse listeners.
        onmousemoved(self.control_paddle)
        onmouseclicked(self.set_ball_velocity)
        # Draw bricks.
        start_x = 0
        start_y = BRICK_OFFSET
        y_column = 1
        while True:
            if start_x < self.window.width - brick_spacing:
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.color = 'pink'
                self.brick.fill_color = 'pink'
                if y_column > 2:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                    if y_column > 4:
                        self.brick.color = 'blue'
                        self.brick.fill_color = 'blue'
                        if y_column > 6:
                            self.brick.color = 'grey'
                            self.brick.fill_color = 'grey'
                            if y_column > 8:
                                self.brick.color = 'purple'
                                self.brick.fill_color = 'purple'
                self.window.add(self.brick, x=start_x, y=start_y)
                start_x = start_x + brick_width + brick_spacing
            else:
                start_y += brick_height+brick_spacing
                y_column += 1
                start_x = 0
                if start_y == BRICK_OFFSET + (brick_height+brick_spacing) * brick_rows:
                    break

        self.total_brick = brick_rows * brick_cols

    # the midpoint of the paddle will the mouse.
    def control_paddle(self, e):
        self.paddle.x = e.x - self.paddle.width/2
        if e.x < self.paddle.width/2:
            self.paddle.x = 0
        elif e.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width

    # when game is over, the ball will go back to where it starts.
    def rest_ball(self):
        self.__dy = 0
        self.__dx = 0
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    # only when the ball is at the start point can click the mouse to start the game.
    def set_ball_velocity(self, event):
        if self.ball.x == (self.window.width-self.ball.width)/2 and self.ball.y == (self.window.height-self.ball.height)/2:
            self.__dx = random.randint(0, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx *= -1

    # Getter
    def get_velocity_x(self):
        return self.__dx

    # Getter
    def get_velocity_y(self):
        return self.__dy

    # If the ball hits the bricks or the paddle, it will bounce and the bricks will be removed at the same time.
    def check_object(self):
        object_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        object_2 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
        object_3 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2)
        object_4 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        if object_1 is not None:
            if object_1 is not self.paddle:
                self.window.remove(object_1)
                self.total_brick -= 1
                self.__dy *= -1
            else:
                if self.__dy > 0:
                    self.__dy *= -1
        elif object_2 is not None:
            if object_2 is not self.paddle:
                self.window.remove(object_2)
                self.total_brick -= 1
                self.__dy *= -1
            else:
                if self.__dy > 0:
                    self.__dy *= -1
        elif object_3 is not None:
            if object_3 is not self.paddle:
                self.window.remove(object_3)
                self.total_brick -= 1
                self.__dy *= -1
            else:
                if self.__dy > 0:
                    self.__dy *= -1
        elif object_4 is not None:
            if object_4 is not self.paddle:
                self.window.remove(object_4)
                self.total_brick -= 1
                self.__dy *= -1
            else:
                if self.__dy > 0:
                    self.__dy *= -1

    def bounce_x(self):
        self.__dx *= -1

    def bounce_y(self):
        self.__dy *= -1








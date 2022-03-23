"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause

import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball
MAX_X_SPEED = 3        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout',
                 lives=100):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.life = lives

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2,
                            y=(window_height-paddle_offset-paddle_height))
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = random.randint(0, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        onmousemoved(self.mouse_move)
        onmouseclicked(self.mouse_click)
        # Death

        # Draw bricks
        anchor_x = 0
        anchor_y = brick_offset
        n = brick_rows * brick_cols
        for i in range(n):
            # create brick
            brick = GRect(brick_width, brick_height)
            brick.filled = True
            brick.fill_color = 'blue'

            # add brick to the anchored position
            if anchor_x == window_width-brick_width:
                self.window.add(brick, x=anchor_x, y=anchor_y)
                anchor_x = 0
                anchor_y += brick_height+brick_spacing
            else:
                self.window.add(brick, x=anchor_x, y=anchor_y)
                anchor_x += brick_width+brick_spacing

    def mouse_move(self, mouse):
        if 0 < mouse.x < self.window.width-self.paddle.width:
            self.paddle.x = mouse.x

    def mouse_click(self, mouse):
        while self.life > 0:
            if self.window.get_object_at(self.ball.x, self.ball.y) is None:
                if self.ball.x < 0 or self.ball.x > self.window.width - self.ball.width:
                    self.__dx = -self.__dx
                if self.ball.y < 0:
                    self.__dy = -self.__dy
                if self.ball.y > self.window.height - self.ball.height:
                    self.life -= 1
                    self.ball.x = self.window.width/2-self.ball.width
                    self.ball.y = self.window.width/2-self.ball.width
            elif self.window.get_object_at(self.ball.x, self.ball.y) is self.paddle \
                    or self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is self.paddle\
                    or self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width) is \
                    self.paddle\
                    or self.window.get_object_at(self.ball.x, self.ball.y+self.ball.width) is self.paddle:
                self.__dy = -self.__dy
            else:
                self.__dy = -self.__dy
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
            self.ball.move(self.__dx, self.__dy),
            pause(1000 / 120)
        self.ball.x = self.window.width/2-self.ball.width
        self.ball.y = self.window.height/2-self.ball.width
        text = GLabel("Game Over", x=self.window.width/2, y=self.window.height*(2/3))
        self.window.add(text)

    def get_speed(self):
        return self.__dx, self.__dy

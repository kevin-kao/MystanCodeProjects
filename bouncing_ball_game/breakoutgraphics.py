"""
stanCode Breakout Project by Kevin
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
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
INITIAL_Y_SPEED = 4    # Initial vertical speed for the ball (default 7)
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.switch = False
        self.radius = ball_radius
        self.label = GLabel('Number of Lives')
        self.break_num = brick_cols * brick_rows

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2,
                       y=self.window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'blue'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(self.radius*2, self.radius*2, x=self.window_width//2-self.radius, y=self.window_height//2)
        self.ball.filled = True
        self.ball.fill_color = 'medium blue'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_is_moving)

        # Draw bricks
        x_init = 0
        y_init = paddle_offset
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=x_init, y=y_init)
                self.brick.filled = True
                if i // 2 == 0:
                    self.brick.fill_color = 'deep sky blue'
                elif i // 2 == 1:
                    self.brick.fill_color = 'light sky blue'
                elif i // 2 == 2:
                    self.brick.fill_color = 'light blue'
                elif i // 2 == 3:
                    self.brick.fill_color = 'aqua'
                else:
                    self.brick.fill_color = 'alice blue'
                self.window.add(self.brick)
                x_init += brick_width+brick_spacing
            x_init = 0
            y_init += brick_height + brick_spacing

    def paddle_move(self, event):
        """
        Create a move for paddle based on the mouse event
        :param event: mouse event
        """
        if event.x+self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x-self.paddle.width/2 <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x-self.paddle.width/2

    def reset_ball(self):
        """
        Reset the ball to the center place and reset the ball velocity
        """
        self.ball.x = self.window_width // 2 - self.radius
        self.ball.y = self.window_height // 2
        self.set_ball_velocity()
        # self.window.add(self.ball)

    # Define vx and vy
    def set_ball_velocity(self):
        """
        reset the ball velocity
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    @property  # another way to specify getter. It's like an attribute: https://www.youtube.com/watch?v=WhaZNMaRuGE
    def dx(self):
        """
        Set a getter for dx to get the dx on the user side
        :return: dx
        """
        return self.__dx

    def get_dy(self):
        """
        Set a getter for dy to get the dy on the user side
        :return: dy
        """
        return self.__dy

    def set_dx(self):
        """
        Change the dx to be negative. The user can use this.
        :return: -dx
        """
        self.__dx = -self.__dx

    def set_dy(self):
        """
        Change the dy to be negative. The user can use this.
        :return: -dy
        """
        self.__dy = -self.__dy

    def ball_is_moving(self, event):
        """
        Make the ball move
        :param event: mouse click
        """
        self.switch = True
        self.set_ball_velocity()

    def switch_off(self):
        """
        Turn the switch off
        """
        self.switch = False
        self.ball.x = self.window_width//2-self.radius
        self.ball.y = self.window_height//2


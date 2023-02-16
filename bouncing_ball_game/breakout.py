"""
stanCode Breakout Project made by Kevin
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The program is to create a ball game where the user clicks on the mouse to start the game and
move the mouse to make the ball rebound and hit the bricks. When the brick is hit by the ball,
that specific brick disappears. There are three chances in the game, meaning that if the ball falls under the paddle
for three times, the game will be over.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_updated import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    lives = NUM_LIVES

    # vx = graphics.get_dx() it will stay the same velocity for the second time or third time
    # vy = graphics.get_dy() so it should be put inside the while true

    while True:
        vx = graphics.dx  # Use property in coder side for getter. It's like an attribute
        vy = graphics.get_dy()
        # print('vx', vx) # to prove that the vx changes for next time
        # print('vy', vy) # to prove that the vy changes for next time
        pause(FRAME_RATE)
        if graphics.switch:  # if the switch is off, start moving the ball
            graphics.ball.move(vx, vy)
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.switch_off()  # turn the switch off if the ball is falling out of the window
                lives -= 1
                if lives == 0:  # No lives. Game over!
                    break
            if graphics.break_num == 0:  # No bricks left. Game over!
                break
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx()   # Bouncing the ball if it's out of the window. No need to write dx = -dx
            if graphics.ball.y <= 0:
                graphics.set_dy()   # Bouncing the ball if it's out of the window. No need to write dy = graphics.set_dy
            check_collision(graphics)  # Check the 4 points to make sure the bouncing activity is set in right place


def check_collision(graphics):
    for x in range(graphics.ball.x, graphics.ball.x + graphics.ball.width+1, graphics.ball.width):
        for y in range(graphics.ball.y, graphics.ball.y + graphics.ball.height+1, graphics.ball.height):
            ball_object = graphics.window.get_object_at(x, y)  # don't put it out of loop
            if ball_object is not None:
                if ball_object == graphics.paddle:
                    if graphics.get_dy() > 0:  # getter. This is to make sure the ball will not vibrate in the paddle
                        graphics.set_dy()  # set dy to be negative to bounce the ball
                else:
                    graphics.window.remove(ball_object)
                    graphics.set_dy()  # set dy to be negative to bounce the ball
                    graphics.break_num -= 1  # to calculate how many bricks are left
                return  # use return to break out of the function, meaning that if there's a collision at one point,
                        # we don't need to check the rest of points


if __name__ == '__main__':
    main()

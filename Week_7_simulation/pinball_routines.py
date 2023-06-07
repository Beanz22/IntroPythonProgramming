#!/usr/bin/env python3

import numpy as np

# YOUR CODE HERE

# ----- iterative systems part II ----------
# These are the routines used in this week's assignments. Copy them, or include this .py file
def acceleration_due_to_gravity():
    """Somewhat silly - but if we need to change it, then we can  change it just here"""
    gravity = -9.8     # m/s
    return gravity


# ------------------------ iterating --------------------------
# Only one method defined for you here - doing one time step
#

# It seems a bit overkill to make a functions for the update, but it *does* make it easier to
#  debug, because you can check if this function is correct with some known values
def compute_next_step(current_state, delta_t=0.1):
    """ How to compute the next position and velocity from this one
    @param current_state - the pose (x, y) and velocity (vx, vy) and acceleration (ax, ay) as a numpy array
    @param delta_t - the time step to use. Define a default t value that you've determined works well
    @return the new position, velocity as a tuple"""

    # TODO: This is compute_next_position_and_velocity from a_tutorial_functions in week 4.
    #  Changes: Keep the pose and the velocity and acceleration in a 3x2 numpy array
    #  Position is position + dt * velocity
    #  Velocity is velocity + dt * acceleration
    #  Acceleration is gravity (optional HWK: Add drag, which is a fraction of velocity in the opposite direction)
    result = np.zeros(current_state.shape)
# YOUR CODE HERE

    return result


# ---------------------- Run into the walls logic/functions ----------
#
# Two options: "Fancy" math using the formula ax + by + c = 0 half plane, or just put the if statements in the
#  individual wall functions
#
#
# This is a generalization trade-off - doing it with a half plane means I could, in theory, make any convex shape
#  instead of just a box... say a trapezoid

# YOUR CODE HERE
    return x_y, vx_vy


# When you're starting, it might be easier to write a function for, eg, JUST the top wall
def outside_top_wall(x_y, y_height):
    """ Did the ball hit the "top" wall?
    @param x_y - position
    @param y_height
    @return True/False"""
    # TODO return true if x_y is on the other side of the wall
# YOUR CODE HERE
    return False


def outside_left_wall(x_y, x_wall):
    """ Did the ball hit the "left" wall?
    @param x_y - position
    @param x_wall
    @return True/False"""
    # TODO return true if x_y is on the other side of the wall
# YOUR CODE HERE
    return False


def outside_right_wall(x_y, x_wall):
    """ Did the ball hit the "right" wall?
    @param x_y - position
    @param x_wall
    @return True/False"""
    # TODO return true if x_y is on the other side of the wall
# YOUR CODE HERE
    return False


# ---------------------- Run into the bumpers functions ----------
#
# Similar to above, except these are circular bumpers, defined by a center x,y and a radius.

# TODO
# Define your own function here for calculating the intersection of the pinball with the bumper

# YOUR CODE HERE


# TODO: Put routines to check answers here
if __name__ == '__main__':
    # walls: top, left, right
    walls = [5.0, -3.0, 3.0]

# YOUR CODE HERE

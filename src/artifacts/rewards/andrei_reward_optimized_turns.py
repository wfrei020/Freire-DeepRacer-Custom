# hyper : discoutn factor - 0.95
import math
def reward_function(params):
    '''
    Example of rewarding the agent to stay inside the two borders of the track
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']  # flag to indicate if the agent is on the track
    distance_from_center = params['distance_from_center']  # float - distance in meters from the track center
    crashed = params['is_crashed']  # Boolean flag to indicate whether the agent has crashed.
    progress = params['progress']  # float - percentage of track completed
    offtrack = params['is_offtrack']  # Boolean flag to indicate whether the agent has gone off track.
    track_width = params['track_width']  # float - width of the track
    speed = params['speed']  # float - agent's speed in meters per second (m/s)
    steps = params['steps']  # int number steps completed
    steering = params['steering_angle']    # agents steerig angle in degrees
    left_of_center = params['is_left_of_center']  # bool if agent left of center

    TOTAL_NUM_STEPS = 300
    if crashed and offtrack:
        reward = -1.0
        return float(reward)

    # if agent is on the left lane and all wheel are not on track and steering angle is to the left penalize
    if not all_wheels_on_track and left_of_center and steering > 0:
        reward = -1.0
        return float(reward)
    # if agent is on the right lane and all wheel are onot on track and steering angle is to the right penalize
    if not all_wheels_on_track and not left_of_center and steering < 0:
        reward = -1.0
        return float(reward)
    # Give a very low reward by default
    reward = 1e-3
    # give reward for proper steering

    if not all_wheels_on_track and left_of_center and steering < 0:
        reward += 2 * math.sin(math.radians(-steering))

    if not all_wheels_on_track and not left_of_center and steering > 0:
        reward += 2 * math.sin(math.radians(steering))

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward += 1.0
        reward += 2**speed
    else:
        reward += 2**(speed**(1 / 2))

    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100:
        reward += 10.0

    # Always return a float value
    return float(reward)


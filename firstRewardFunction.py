#Time trial - Jochem Turnpike

# First Training - 2 Hours
# Based on: https://github.com/scottpletcher/deepracer/blob/master/iterations/v4-SelfMotivator.md
# Successfully completed 3 laps without getting off-track @ 2:37.525
# Speed: 0.6 - 1 m/s

def reward_function(params):

    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.001
        
    return float(reward)

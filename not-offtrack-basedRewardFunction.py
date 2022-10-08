#Time trial - Jochem Turnpike

# Second Training - 3 Hours
# Based on a tip by Firefist Ace at AWS Machine Learning Community Slack Channel
# "all wheels on track would mean it would get penalty even if one wheel goes out of track" and "we dont want that" [sic]

# Successfully completed 3 laps without getting off-track @ 2:29.988 but I cancelled the training in hopes of submitting this model before the 12:00 pm deadline.
# Creation Time: Sep 30th 2022, 9:53 am

def reward_function(params):

    if not params['is_offtrack'] and params['steps'] > 0:
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.001
        
    return float(reward)

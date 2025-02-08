"""
     Our illustration of the Bayes filter algorithm is based on a scenario,
 where a robot estimating the state of a door using its camera. To make this
 problem simple, let us assume that the door can be in one of two possible states, open
 or closed, and that only the robot can change the state of the door. Let us furthermore
 assume that the robot does not know the state of the door initially. Instead, it assigns
 equal prior probability to the two possible door states

    bel(X0 = open) = 0.5
    bel(X0 = closed) = 0.5


    Let us furthermore assume the robot's sensors are noisy. The noise is characterized by
 the following conditional probabilities:

    p(Zt = sense_closed | Xt = is_open  ) = 0.6
    p(Zt = sense_open   | Xt = is_open  ) = 0.4
    p(Zt = sense_open   | Xt = is_closed) = 0.2
    p(Zt = sense_closed | Xt = is_closed) = 0.8
"""

belief_door_closed = 0.5
belief_door_open = 1- belief_door_closed


import matplotlib.pyplot as plt
import numpy as np
from cannon import Cannon
from filters import InformationFilterLinear

# Simulation parameters
timeslice = 0.1
iterations = 144
gravity = np.array([0, -9.81])
wind = np.array([0, 0])
noiselevel = 10
muzzle_velocity = 100
angle = 45

# Matrices
state_transition = np.array([[1, timeslice, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, timeslice],
                             [0, 0, 0, 1]])
control_matrix = np.eye(4)
control_vector = np.array([
    0.5 * (wind[0] + gravity[0]) * timeslice**2,
    (wind[0] + gravity[0]) * timeslice,
    0.5 * (wind[0] + gravity[1]) * timeslice**2,
    (wind[1] + gravity[1]) * timeslice
])
observation_matrix = np.eye(4)
initial_state = np.array([0, muzzle_velocity * np.cos(np.radians(angle)),
                          np.random.randint(0, 251), muzzle_velocity * np.sin(np.radians(angle))])
initial_probability = np.eye(4)
process_covariance = np.zeros((4, 4))
measurement_covariance = np.eye(4) * 0.8

# Simulation
c = Cannon(angle, muzzle_velocity, gravity, wind, timeslice, noiselevel)
kf = InformationFilterLinear(state_transition, control_matrix, observation_matrix,
                        initial_state, initial_probability, process_covariance, measurement_covariance)

true_x, true_y, measure_x, measure_y, pred_x, pred_y = [], [], [], [], [], []

for _ in range(iterations):
    true_x.append(c.get_x())
    true_y.append(c.get_y())
    measure_x.append(c.get_x_with_noise())
    measure_y.append(c.get_y_with_noise())

    cur_state = kf.get_current_state()
    pred_x.append(cur_state[0])
    pred_y.append(cur_state[2])

    c.step()
    measurement_vector = np.array([measure_x[-1], cur_state[1], measure_y[-1], cur_state[3]])
    kf.step(control_vector, measurement_vector)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(true_x, true_y, 'g-', label='True Path')
plt.plot(measure_x, measure_y, 'r*', label='Noisy Measurements')
plt.plot(pred_x, pred_y, 'b-', label='Kalman Filter Prediction')
plt.xlabel('X position')
plt.ylabel('Y position')
plt.title('Measurement of a Cannonball in Flight')
plt.legend()
plt.grid()
plt.show()


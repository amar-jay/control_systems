import numpy as np

class KalmanFilterLinear:
    def __init__(self, A, B, C, x, P, Q, R):
        self.A = np.array(A)  # State transition matrix
        self.B = np.array(B)  # Control matrix
        self.C = np.array(C)  # Observation matrix
        self.current_state_estimate = np.array(x)  # Initial state estimate
        self.current_prob_estimate = np.array(P)  # Initial covariance estimate
        self.Q = np.array(Q)  # Estimated error in process
        self.R = np.array(R)  # Estimated error in measurements

    def get_current_state(self):
        return self.current_state_estimate

    def step(self, control_vector, measurement_vector):
        control_vector = np.array(control_vector)
        measurement_vector = np.array(measurement_vector)
        
        # Prediction step
        predicted_state_estimate = self.A @ self.current_state_estimate + self.B @ control_vector
        predicted_prob_estimate = self.A @ self.current_prob_estimate @ self.A.T + self.Q
        
        # Observation step
        innovation = measurement_vector - self.C @ predicted_state_estimate
        innovation_covariance = self.C @ predicted_prob_estimate @ self.C.T + self.R
        
        # Update step
        kalman_gain = predicted_prob_estimate @ self.C.T @ np.linalg.inv(innovation_covariance)
        self.current_state_estimate = predicted_state_estimate + kalman_gain @ innovation
        
        # Update covariance estimate
        size_est = self.current_prob_estimate.shape[0]
        self.current_prob_estimate = (np.eye(size_est) - kalman_gain @ self.C) @ predicted_prob_estimate

class InformationFilterLinear:
    def __init__(self, A, B, C, x, P, Q, R):
        self.A = np.array(A)  # State transition matrix
        self.B = np.array(B)  # Control matrix
        self.C = np.array(C)  # Observation matrix
        self.current_state_estimate = np.array(x)  # Initial state estimate
        self.current_prob_estimate = np.array(P)  # Initial covariance estimate
        self.info_matrix = np.array(np.linalg.inv(P))  # Initial Mahalanobis distance
        self.info_state = np.array(np.linalg.inv(P) @ x)  # Initial covariance estimate
        self.Q = np.array(Q)  # Estimated error in process
        self.R = np.array(R)  # Estimated error in measurements

    def get_current_state(self):
        return self.current_state_estimate

    def step(self, control_vector, measurement_vector):
        control_vector = np.array(control_vector)
        measurement_vector = np.array(measurement_vector)
        
        # Prediction step
        predicted_state_estimate = self.A @ np.linalg.inv(self.info_matrix) @ self.info_state + self.B @ control_vector
        
        # Observation step
        predicted_info_matrix = np.linalg.inv(self.A @ self.current_state_estimate @ self.A.T + self.R)
        predicted_info_state = predicted_info_matrix @ predicted_state_estimate
        
        # Update step
        z = self.C.T @ np.linalg.inv(self.Q)
        self.info_matrix = z @ self.C + predicted_info_matrix
        self.info_state = z @ measurement_vector + predicted_info_state

        self.current_prob_estimate = np.linalg.inv(self.info_matrix)
        self.current_state_estimate = self.current_prob_estimate @ self.info_state


class InformationFilterExtended:
    def __init__(self, g, h,G, H, x, P, Q, R):
        self.g = g # state nonlinear function
        self.h = h # Control function
        self.G = np.array(G)  # Observation matrix
        self.H = np.array(H)  # Observation matrix
        self.current_state_estimate = np.array(x)  # Initial state estimate
        self.current_prob_estimate = np.array(P)  # Initial covariance estimate
        self.info_matrix = np.array(np.linalg.inv(P))  # Initial Mahalanobis distance
        self.info_state = np.array(np.linalg.inv(P) @ x)  # Initial covariance estimate
        self.Q = np.array(Q)  # Estimated error in process
        self.R = np.array(R)  # Estimated error in measurements

    def get_current_state(self):
        return self.current_state_estimate

    def step(self, control_vector, measurement_vector):
        control_vector = np.array(control_vector)
        measurement_vector = np.array(measurement_vector)
        
        # Prediction step
        previous_state = np.linalg.inv(self.info_matrix) @ self.info_state
        predicted_info_matrix = np.linalg.inv(self.G @ np.linalg.inv(self.info_matrix) @ self.G.T + self.R)
        
        # Observation step
        predicted_mean = self.g(control_vector, previous_state)
        predicted_info_state = predicted_info_matrix @ predicted_mean
        
        # Update step
        z = self.H.T @ np.linalg.inv(self.Q)
        self.info_matrix = z @ self.H + predicted_info_matrix
        self.info_state = z @ (measurement_vector -self.h(predicted_mean) + self.H @ predicted_mean) + predicted_info_state

        self.current_prob_estimate = np.linalg.inv(self.info_matrix)
        self.current_state_estimate = self.current_prob_estimate @ self.info_state

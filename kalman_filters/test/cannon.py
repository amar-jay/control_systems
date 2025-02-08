import numpy as np

class Cannon:
    def __init__(self, angle, muzzle_velocity, gravity, wind, time_slice, noise_level):
        """
            angle              The angle from the ground to point the cannon.
            muzzle_velocity    Muzzle velocity of the cannon.
            gravity            A vector containing gravitational acceleration.
            wind               A vector containing wind force
            velocity           The initial velocity of the cannonball
            loc                The initial location of the cannonball.
            acceleration       The initial acceleration of the cannonball.
            timeslice          The timeslice (dt)
            noiselevel         Maximum noise added to the original measurements.
        """
        self.timeslice = time_slice
        self.noiselevel = noise_level
        self.angle = angle
        self.muzzle_velocity = muzzle_velocity
        
        # Parameters affecting cannonball flight
        self.gravity = np.array(gravity)
        self.wind = np.array(wind)
        
        # Initial velocity components
        self.velocity = np.array([
            self.muzzle_velocity * np.cos(np.radians(self.angle)),
            self.muzzle_velocity * np.sin(np.radians(self.angle))
        ])
        
        # Initial location and acceleration
        self.loc = np.array([0.0, 0.0])
        self.acceleration = np.array([0.0, 0.0])

    def get_x(self):
        return self.loc[0]

    def get_y(self):
        return self.loc[1]

    def get_x_with_noise(self):
        return np.random.normal(self.loc[0], self.noiselevel)

    def get_y_with_noise(self):
        return np.random.normal(self.loc[1], self.noiselevel)

    def get_x_velocity(self):
        return self.velocity[0]

    def get_y_velocity(self):
        return self.velocity[1]

    def step(self):
        # Break forces into smaller time slices
        sliced_gravity = self.gravity * self.timeslice
        sliced_wind = self.wind * self.timeslice
        
        # Compute acceleration
        sliced_acceleration = sliced_gravity + sliced_wind
        
        # Update velocity
        self.velocity += sliced_acceleration
        
        # Break velocity into time slice
        sliced_velocity = self.velocity * self.timeslice
        
        # Update location
        self.loc += sliced_velocity
        
        # Prevent the cannonball from going underground
        if self.loc[1] < 0:
            self.loc[1] = 0


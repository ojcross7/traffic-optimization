import numpy as np  
from stable_baselines3 import PPO  

class RLOptimizer:  
    def __init__(self, env):  
        self.model = PPO("MlpPolicy", env, verbose=1)  

    def train(self, timesteps=10000):  
        self.model.learn(total_timesteps=timesteps)  

    def predict_optimal_signal(self, observation):  
        action, _ = self.model.predict(observation)  
        return action  
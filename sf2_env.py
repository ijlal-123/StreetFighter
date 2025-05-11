import gym
import retro
import numpy as np
import cv2

class StreetFighterCustomEnv(gym.Env):
    def __init__(self):
        super(StreetFighterCustomEnv, self).__init__()
        self.env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(84, 84, 1), dtype=np.uint8)
        self.action_space = self.env.action_space

    def preprocess(self, obs):
        obs = cv2.cvtColor(obs, cv2.COLOR_RGB2GRAY)  # Grayscale
        obs = cv2.resize(obs, (84, 84))              # Resize
        obs = np.expand_dims(obs, axis=-1)           # Add channel dimension
        return obs

    def reset(self):
        obs = self.env.reset()
        return self.preprocess(obs)

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        return self.preprocess(obs), reward, done, info

    def render(self, mode='human'):
        self.env.render()

    def close(self):
        self.env.close()

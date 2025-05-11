from stable_baselines3 import PPO
from sf2_env import StreetFighterCustomEnv

# Load trained model
model = PPO.load("ppo_streetfighter")

# Create environment
env = StreetFighterCustomEnv()

obs = env.reset()
while True:
    action, _ = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()

    if done:
        obs = env.reset()

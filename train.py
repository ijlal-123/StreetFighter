from stable_baselines3 import PPO
from sf2_env import StreetFighterCustomEnv

# Create environment
env = StreetFighterCustomEnv()

# Create PPO model
model = PPO("CnnPolicy", env, verbose=1, tensorboard_log="./ppo_sf2_tensorboard/")

# Train the model
model.learn(total_timesteps=10000)  # 100k steps (adjust as you want)

# Save the model
model.save("ppo_streetfighter")

# Close environment
env.close()

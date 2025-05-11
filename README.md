
# 🕹️ Street Fighter II Reinforcement Learning Agent

This project implements a reinforcement learning agent trained to play **Street Fighter II** using the **Proximal Policy Optimization (PPO)** algorithm. The environment is built using [Gym-Retro](https://github.com/openai/retro), and training is done using [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3).

---

## 📽️ Demo
👉 *Coming soon: Video of the trained agent defeating the AI opponent!*

---

## 📌 Project Overview

- **Game**: Street Fighter II (Champion Edition)
- **AI Approach**: Proximal Policy Optimization (PPO)
- **Environment**: Gym-Retro with custom wrappers
- **Goal**: Train an AI agent to defeat a fixed in-game AI opponent by learning optimal strategies through trial-and-error

---

## 🧠 Reinforcement Learning Setup

- **Algorithm**: PPO (Stable-Baselines3)
- **Observation Space**: Downsampled game frames or custom game-specific features
- **Action Space**: Reduced set of meaningful actions (e.g., punch, kick, block, move)
- **Reward Function**:
  - +1 for dealing damage
  - -1 for taking damage
  - +10 for winning a round
  - -10 for losing a round
  - Small penalty for idle time

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ijlal-123/StreetFighter.git
cd StreetFighter
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Gym-Retro and Setup the Game ROM

```bash
pip install gym-retro
python -m retro.import ./roms/
```

> 📁 Place your `StreetFighterII.smc` ROM file inside the `roms/` directory.

---

## 🏃‍♂️ Running the Agent

### Train the PPO Agent

```bash
python train_agent.py
```

### Evaluate the Trained Model

```bash
python evaluate_agent.py
```

---

## 📊 Results

After training for several million steps, the agent achieved:

- **~80% win rate** against the fixed AI
- Learned to block attacks, combo moves, and trap the opponent
- Real-time decision making within frame limits

---

## 👥 Team Members

- **Ijlal Iqbal (22K-5034)** – PPO implementation and training logic  
- **Huzefa Saifuddin (22K-5125)** – Environment setup, Gym-Retro integration  
- **Areeb ur Rehman (22K-6003)** – Reward design, evaluation, and performance tuning  

---

## 📚 References

- [OpenAI Gym Retro](https://github.com/openai/retro)
- [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3)
- Sutton & Barto – *Reinforcement Learning: An Introduction*
- PPO Paper – [Schulman et al. (2017)](https://arxiv.org/abs/1707.06347)

---

## 📄 License

MIT License. See `LICENSE` file for details.

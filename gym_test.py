
import gymnasium as gym
env = gym.make('CartPole-v1')


observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)
    print(observation)
    print(reward)

    if terminated or truncated:
        observation, info = env.reset()

env.close()
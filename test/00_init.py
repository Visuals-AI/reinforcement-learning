
import gymnasium as gym

# 查看所有可以创建的环境
# 官方预设的学习环境，实际上 env 应该自己根据游戏交互接口和观察接口实现
envs = gym.envs.registry.keys()
print(envs)

# 月球登录车
# 初始化环境，返回的 env 主要用于用户交互
env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()

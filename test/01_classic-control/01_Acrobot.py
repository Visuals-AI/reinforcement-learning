# http://incompleteideas.net/book/11/node4.html

import gymnasium as gym
env = gym.make('Acrobot-v1')

# To change the dynamics as described above
env.unwrapped.book_or_nips = 'nips'

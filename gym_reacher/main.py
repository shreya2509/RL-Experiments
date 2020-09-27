import gym
import numpy as np
from ddpg_torch import Agent
from utils import plot_learning_curve


env = gym.make('LunarLanderContinuous-v2')


for i in range(0,2):
	observation=env.reset()
	done=0
	while not done:
		env.render()
		action=env.action_space.sample()
		observation,reward,done,info=env.step(action)
		print(action,observation,reward)
env.close()



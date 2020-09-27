import gym
import numpy as np
from ddpg_torch import Agent
from utils import plot_learning_curve
from env import env
import turtle
from random_movement import Prey
import time

if __name__ == '__main__':  

    # create window  
    win = turtle.Screen()
    win.title('Simple')
    win.bgcolor('black')
    win.tracer(0)
    win.setup(width=600,height=600)
 
    
    #create env and object to track
    E = env()
    track = Prey()

    # create ddpg
    agent = Agent(alpha=0.0001, beta=0.001, 
                    input_dims=[6], tau=0.001,
                    batch_size=64, fc1_dims=400, fc2_dims=300, 
                    n_actions=2)
    agent.load_models()
    
    n_games = 5
    score_history = []

    for i in range(n_games):

        observation = E.reset()
        done = 0
        score = 0
        #agent.noise.reset()
        cntr = 0

        while not done:
            action = agent.choose_action(observation)
            #print(action)
            if(action[0]<0):
                v = 4
            elif(action[0]==0):
                v = 5
            else:
                v = 6
            observation_, reward, done = E.step(action)
            agent.remember(observation, action, reward, observation_, done)
            #agent.learn()
            reward = -(cntr)
            score += reward
            observation = observation_
            cntr+=1
            observation[4],observation[5]=track.step()
            win.update()
        print('score of the episode',score)
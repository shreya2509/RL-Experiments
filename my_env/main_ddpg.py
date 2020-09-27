import gym
import numpy as np
from ddpg_torch import Agent
from utils import plot_learning_curve
from env import env
import turtle
import time
from random_movement import Prey
if __name__ == '__main__':
    #env = gym.make('LunarLanderContinuous-v2')

       
    win = turtle.Screen()
    win.title('Simple')
    win.bgcolor('black')
    win.tracer(0)
    win.setup(width=600,height=600)

    
    E = env()
    track = Prey()
    agent = Agent(alpha=0.0001, beta=0.001, 
                    input_dims=[6], tau=0.001,
                    batch_size=64, fc1_dims=400, fc2_dims=300, 
                    n_actions=2)
    #agent.load_models()
    n_games = 300
    filename = 'MyEnv_alpha_' + str(agent.alpha) + '_beta_' + \
                str(agent.beta) + '_' + str(n_games) + '_games'
    figure_file = 'plots/' + filename + '.png'

    best_score = -600
    score_history = []
    for i in range(n_games):
        observation = E.reset()
        done = False
        score = 0
        agent.noise.reset()
        cntr = 0
        while not done:
            action = agent.choose_action(observation)
            #print(action)
            if(action[0]<0):
                action[0] = 4
            elif(action[0]==0):
                action[0] = 5
            else:
                action[0] = 6



            #action[1]=action[1]*3.14

            observation_, reward, done = E.step(action)
            agent.remember(observation, action, reward, observation_, done)
            agent.learn()
            reward = reward-cntr
            score += reward
            observation = observation_
            cntr+=0.1
            observation[4],observation[5]=track.step()
            #print(reward,observation,done)
            win.update()
            #time.sleep(0.1)

        score_history.append(score)
        avg_score = np.mean(score_history[-10:])

        if avg_score > best_score:
            best_score = avg_score
            agent.save_models()

        print('episode ', i, 'score %.1f' % score,
                'average score %.1f' % avg_score)
    x = [i+1 for i in range(n_games)]
    
    plot_learning_curve(x, score_history, figure_file)
       




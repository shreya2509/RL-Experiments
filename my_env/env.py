import numpy as np 
import turtle
from Agent import A
import time

class env(object):

	def __init__(self):
		self.ai = A(ini_position=(0,0),ini_velocity=5,ini_heading=0.5)
		self.ai.create()
		self.state=[0,0,5,0,200,-100]
		# state [initial_agent_x, y, v, heading, target_x,target_y]
		self.done=0
		self.reward=0

	def reset(self):
		return self.state

	def step(self,action):
		self.state[0],self.state[1], self.state[2], self.state[3],self.reward,self.done=self.ai.aistep(action,self.state)
		
		#time.sleep(0.1)

		#0],self.state[1], self.state[2], self.state[3],self.state[4]

		#dis = np.sqrt((self.state[0]-self.state[4])**2+(self.state[1]-self.state[5])**2)
		'''
		if (dis<50):
			self.reward = 1000

		elif(dis<280 and dis>50):
			self.reward = ((dis/283)*40)-20
		else:
			self.reward = -20
		'''
		
		return self.state,self.reward,self.done


		


'''

if __name__ == '__main__':

	win = turtle.Screen()
	win.title('Simple')
	win.bgcolor('black')
	win.tracer(0)
	win.setup(width=600,height=600)
	track = turtle.Turtle()      # Create a turtle object
	track.speed(0)
	track.shape('circle') 
	track.color('red')           # Set the color to red
	track.penup()
	track.goto(200,200)

	E = env()



	for i in range(10):
		done = 0
		score = 0 
		while not done:
			state,reward,done = E.step([0.1,0.1])
			score+=reward
			print("reward",reward)
			win.update()
			time.sleep(0.1)
		print("The score of episode  is: ",score)

'''

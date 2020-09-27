import turtle
import numpy as np 
import time


# assume the state to be an array [ agent velocity, agent heading, target position ]
# reward option 1. propotional to the distance from the target 
#				2. +100 to reach the goal otherwise - 1 for each step



class A(object):

	def __init__(self, ini_position, ini_velocity,ini_heading):
		self.x=ini_position[0]
		self.y=ini_position[1]
		self.v=ini_velocity
		self.heading=ini_heading


	def create(self):
		self.agent = turtle.Turtle()
		self.agent.shape('circle')
		self.agent.penup()
		self.agent.color('white')
		self.agent.speed(self.v)
		self.agent.goto(self.x,self.y)
		#self.reward=0

	def aistep(self,action,state):
		#print(action)
		done = 0
		reward = 0
		dv = action[0]
		#dtheta = action[1]
		dtheta = action[1]*3.14
		#print(theta)

		self.v = dv#+=dv
		self.heading=dtheta
		self.x=self.x+(self.v*np.cos(self.heading))
		self.y=self.y+(self.v*np.sin(self.heading))

		#self.agent.left(dtheta)
		#self.agent.forward(self.v)
		#self.x = self.agent.position()[0]
		#self.y = self.agent.position()[1]

		#self.agent.setposition(self.x,self.y)

		dis = np.sqrt((self.x-state[4])**2+(self.y-state[5])**2)
#		dis_prev = np.sqrt((self.x-state[4])**2+(self.y-state[5])**2)



		reward = -dis/141

		if (dis<25):
			reward = 100
		

		if (self.x>290 or self.x< -290 or self.y>290 or self.y< -290 or dis<25):
			done = 1
			self.x = 0
			self.y = 0
			self.heading = 0
			#self.agent.setposition(0,0)
			self.v = 5
			#self.heading=(self.heading+3.14)%6.28
			#x = np.random.randint(-200,200)
			#y = np.random.randint(-200,200)
			#self.x=self.x+(10*np.cos(self.heading))
			#self.y=self.y+(10*np.sin(self.heading))
		#else:
		self.agent.setposition(self.x,self.y)
		#if done:
			#x = np.random.randint(-290,290)
			#y = np.random.randint(-290,290)
		#	self.agent.setposition(0,0)
		return self.x,self.y,self.v,self.heading,reward,done





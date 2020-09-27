import turtle
from random import uniform
import time


class Prey(object):
	def __init__(self):
		self.prey = turtle.Turtle()
		self.prey.speed(1)
		self.prey.shape('circle')
		self.prey.color('red')
		self.prey.penup()
		self.prey.setposition(100,100)

	def step(self):
		a = uniform(-30,30)
		self.prey.left(a)
		self.prey.setposition(100,100)
		#d = uniform(5,9)
		#self.prey.forward(5)
		#if(self.prey.position()[0]>290 or self.prey.position()[0]< -290 or self.prey.position()[1]>290 or self.prey.position()[1]< -290):
		#	self.prey.setposition(0,0)
		return self.prey.position()[0],self.prey.position()[1]
		#,(self.prey.heading()/360)*3.14
	


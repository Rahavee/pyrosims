import math
import random
import pyrosim
from robot import ROBOT

class INDIVIDUAL:
	def __init__(self):
		self.genome = random.random()*2-1
		self.fitness = 0
		

	def Evaluate(self,pb):
		self.sim = pyrosim.Simulator(window_size = (1500,1500), play_paused=False, eval_time=500, play_blind=pb)
		self.robot=ROBOT(self.sim, self.genome)
		self.sim.start()
		self.sim.wait_to_finish()
		self.y = self.sim.get_sensor_data(sensor_id = self.robot.P4, svi=1)
		self.fitness = self.y[-1]
	
	def Mutate(self):
		self.genome = random.gauss(self.genome, math.fabs(self.genome))
	

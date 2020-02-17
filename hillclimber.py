import pyrosim
import threading
import matplotlib.pyplot as plt
import random
import pickle
import copy
from robot import ROBOT
from individual import INDIVIDUAL


parent = INDIVIDUAL()
parent.Evaluate(False)
for i in range (0,100):
	child=copy.copy(parent)
	child.Mutate()
	child.Evaluate(True)
	print("[g: ",i+1,"] [pw: ",parent.genome,"[p: ", parent.fitness, "] [c: ", child.fitness, "]")
	if (child.fitness > parent.fitness ):
		f=open('robot.p','w')
		pickle.dump(child,f)
		child.Evaluate(False)
		parent = child
		f.close()

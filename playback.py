from individual import INDIVIDUAL
import pickle

f=open("robot.p","r")
best=pickle.load(f)
f.close()
best.Evaluate()
print("[fitness: ", best.fitness "]")

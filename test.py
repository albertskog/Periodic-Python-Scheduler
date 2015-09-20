from periodic_scheduler import periodicTask
import time

def testTask():

	print "Test"

	return False

myTask = periodicTask(1, testTask, repetitions = 5)

time.sleep(3)

myTask.stop()
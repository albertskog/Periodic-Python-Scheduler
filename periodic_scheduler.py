import sched
import time
import thread
import threading

# Periodic task scheduler
class periodicTask:

	def __init__(self, periodSec, task, taskArguments = (), repetitions = 0):

		self.thread = threading.Thread(target = self.threadEntryPoint, 
									   args = (periodSec, task, taskArguments, repetitions))
		self.thread.start()


	def threadEntryPoint(self, periodSec, task, taskArguments, repetitions):

		self.repetitions = repetitions
		self.scheduler = sched.scheduler(time.time, time.sleep)
		self.periodic(self.scheduler, periodSec, task, taskArguments)
		self.scheduler.run()


	def periodic(self, scheduler, delaySec, task, taskArguments):

	  	# Schedule another recursive event
	 	nextEvent = self.scheduler.enter(delaySec, 
	 									 1, 
	 									 self.periodic, 
	 									 (self.scheduler, interval, task, taskArguments))

	 	# Do task and get return status
		stopTask = task(*taskArguments)

		# Stop task if it returned true
	 	if (stopTask == True):
			self.scheduler.cancel(nextEvent)

		self.repetitions = self.repetitions - 1

		# Stop if we ran through all repetitions
		# If repetitions was initialized to 0, run forever (or at least until integer underflow)
		if (self.repetitions == 0):
			self.scheduler.cancel(nextEvent)



def testTask():

	print "Test"

	return False

myTask = periodicTask(1, testTask, repetitions = 3)


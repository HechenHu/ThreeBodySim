import matplotlib.pyplot as plt 
import numpy as np
#divisorsCalculate
def returnNumberOfDivisors(number):
	i = 0
	divisorsCount = 0
	if ((number%2)==0):
		for i in xrange(1,np.sqrt(number)):
			if number%i==0:
				divisorsCount+=1
		return divisorsCount
	if (number%3==0):	
		for i in xrange(1,np.sqrt(number)):
			if number%i==0:
				divisorsCount+=1
		return divisorsCount			
	if (number%5==0):	
		for i in xrange(1,np.sqrt(number)):
			if number%i==0:
				divisorsCount+=1
		return divisorsCount		
	if (number%7==0):	
		for i in xrange(1,np.sqrt(number)):
			if number%i==0:
				divisorsCount+=1
		return divisorsCount		
	else:
		return -1
	return divisorsCount

i = 0
for i in xrange(1,1000):
	if returnNumberOfDivisors(i)!=-1:
		plt.scatter(i,returnNumberOfDivisors(i),c=1,)
		print i ," has ",returnNumberOfDivisors(i)," number of divisors ",np.log(returnNumberOfDivisors(i)) 
		plt.show()
		plt.scatter(i,np.log(returnNumberOfDivisors(i)),c=60, cmap='viridis')
		plt.show()

# -*- coding: utf-8 -*-
import numpy as np
'''
All  functions  accept inputs as SI(Système International d'Unités,or International Standard Units in English)
e.g:meter,kilogram,second.
'''
timeinterval = 0.001
Gvalue = 6.67408e-11
time = 0.00

class _3DVector:
	"""docstring for __3DVector"""
	def __init__(self, X,Y,Z):
		self.x = float(X)
		self.y = float(Y)
		self.z = float(Z)

	def __add__(self,other):
		if other.__class__.__name__ == "_3DVector":
			return _3DVector(float(self.x+other.x),float(self.y+other.y),float(self.z+other.z))
		else:
			return 	_3DVector(float(self.x+other),float(self.y+other),float(self.z+other))

	def __sub__(self,other):
		if other.__class__.__name__ == "_3DVector":
			return _3DVector(float(self.x-other.x),float(self.y-other.y),float(self.z-other.z))
		return 	_3DVector(float(self.x-other),float(self.y-other),float(self.z-other))

	def __iadd__(self,other):
		if other.__class__.__name__=="_3DVector":
			self.x+=other.x
			self.y+=other.y
			self.z+=other.z
			return
		self.x+=other
		self.y+=other
		self.z+=other
		return	

	def __isub__(self,other):
		if other.__class__.__name__=="_3DVector":
			self.x-=other.x
			self.y-=other.y
			self.z-=other.z
			return
		self.x-=other
		self.y-=other
		self.z-=other
		return	
		
	def __mul__(self,other):	
		if other.__class__.__name__!="_3DVector":
			return _3DVector(float(self.x*other),float(self.y*other),float(self.z*other))
		else:
			return _3DVector(0.0,0.0,0.0)
		
	def __imul__(self,other):
		if other.__class__.__name__!="_3DVector":
			self.x*=other
			self.y*=other
			self.z*=other
			return
		return False

	def __pow__(self,other):
		if other==2:
			return np.square(self.x)+np.square(self.y)+np.square(self.z)
		if other>=2:
			return (self**2)*(other//2)+other%2*self
		pass

	def __div__(self,other):
		if (other.__class__.__name__!="_3DVector")&(other!=0):
			return _3DVector(self.x/other,self.y/other,self.z/other)
		return False

	def __eq__(self,other):
		if other.__class__.__name__=="_3DVector":
			self.x = other.x
			self.y = other.y
			self.z = other.z
			return
		return
class Star:
	"""docstring for Star"""
	def __init__(self,xPos,yPos,zPos,mass):
		self.Pos = _3DVector(xPos,yPos,zPos)
		self.Spd = _3DVector(0.00,0.00,0.00)
		self.Gravity = _3DVector(0.00,0.00,0.00)
		self.Accelarate = _3DVector(0.00,0.00,0.00)
		self.Mass = float(mass)
		self.Route= [_3DVector(xPos,yPos,zPos)]

	def GravityCalc(self,*stars):
		grav = _3DVector(0,0,0)
		for s in stars:
			self.Gravity = self.Gravity+(Gvalue*(s.Mass*self.Mass))/(self.Pos-s.Pos)**2
		self.Gravity = grav

	def SpdCalc(self):
		self.Accelarate = self.Gravity/self.Mass
		self.Spd += self.Accelarate

	def RK4PosCalc(self):
		deltaTime = 0.00000000000000000000001
		self.Pos = self.Pos+self.Gravity
		self.Pos = self.Pos+deltaTime/6*(self.Spd+2*(self.Spd+deltaTime/2*self.Accelarate)+2*deltaTime*(self.Spd+deltaTime/2*self.Accelarate)+2*deltaTime**2*(self.Spd+deltaTime/2*self.Accelarate))
		self.Route.append(self.Pos)

def ThreeBodyRoute(time,s1,s2,s3):
	for x in xrange(1,int(time/timeinterval)):
		s1.GravityCalc(s2,s3)
		s2.GravityCalc(s1,s3)
		s3.GravityCalc(s1,s2)
		s1.SpdCalc()
		s2.SpdCalc()
		s3.SpdCalc()
		s1.RK4PosCalc()
		s2.RK4PosCalc()
		s3.RK4PosCalc()
	print s1.Route	
	

s1 = Star(1000,20000,30000,100000000000)
s2 = Star(1000,2000,3000,600000000000)
s3 = Star(10000,20000,30000,300000000000)
ThreeBodyRoute(10,s1,s2,s3)

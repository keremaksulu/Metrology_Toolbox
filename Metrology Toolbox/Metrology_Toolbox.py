import scipy
import matplotlib.pyplot as plt

f = open('data.txt','r')   
x = []
y = []
i = 0
line = '0'

while True :
    line = f.readline()
    if line == '':
        break
    
    x.append(float(line))
    y.append(float(line))

#Natural cubic spline    
ncs = scipy.interpolate.CubicSpline(x,y,bc_type=((2, 0.0), (2, 0.0)))

while i < len(y):
    y[i]=ncs(i)
    i+=1

#Trapezodial integration
trap = scipy.integrate.trapezoid(x,y)

#Calculating the parameters
ra = trap / (x[(len(x)-1)] - x[0])
rq = (trap / (x[(len(x)-1)] - x[0])) ** 0.5

print(ra)
print(rq)
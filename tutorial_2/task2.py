import numpy as np
import matplotlib.pyplot as plt
x= np.array([1,2,3])
y=np.array([1.2,1.9,3.2])

def values(x,y):
	a=x.sum()
	b=y.sum()
	c=(x*x).sum()
	d=(y*y).sum()
	e=len(x)
	w0=(c*b-a*d)/(c*e-a*a)
	w1=(b-(e*w0))/a
	return w1,w0
slope,intercept=values(x,y)
final_values=[slope*i+ intercept for i in x]

plt.title("Maximum Likelihood Linear Line")
plt.xlabel("Data Points")
plt.ylabel("Fitted Points")
plt.scatter(x,y)
plt.plot(x,y,'co')
plt.plot(x,final_values,'y')
plt.show() 
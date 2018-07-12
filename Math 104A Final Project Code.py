# Codes Part 1

import math

def f(t):
    return 1/2*(math.sin(10+t)-math.sin(10-t))

def df(t):
    return 1/2*(math.cos(10+t)+math.cos(10-t))

def cubicspline(n,xn,an,fpo,fpn):
  h=[0]*(n+1)
  alpha=[0]*(n+1)
  l=[0]*(n+1)
  z=[0]*(n+1)
  u=[0]*(n+1)
  c=[0]*(n+1)
  b=[0]*(n+1)
  d=[0]*(n+1)
  for i in range(n):
    h[i]=xn[i+1]-xn[i]
  alpha[0]=3*(an[1]-an[0])/h[0]-3*fpo
  alpha[n]=3*fpn-3*(an[n]-an[n-1])/h[n-1]
  for i in range(1,n):
    alpha[i]=3/h[i]*(an[i+1]-an[i])-3/h[i-1]*(an[i]-an[i-1])
  l[0]=2*h[0]
  u[0]=0.5
  z[0]=alpha[0]/l[0]
  for i in range(1,n):
    l[i]=2*(xn[i+1]-xn[i-1])-h[i-1]*u[i-1]
    u[i]=h[i]/l[i]
    z[i]=(alpha[i]-h[i-1]*z[i-1])/l[i]
  l[n]=h[n-1]*(2-u[n-1])
  z[n]=(alpha[n]-h[n-1]*z[n-1])/l[n]
  c[n]=z[n]
  for j in range(n-1,-1,-1):
    c[j]=z[j]-u[j]*c[j+1]
    b[j]=(an[j+1]-an[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3
    d[j]=(c[j+1]-c[j])/(3*h[j])
  for j in range (n):
    print("j=",j,an[j],b[j],c[j],d[j])

x_vec=[0,1,2]
a_vec=[f(0), f(1), f(2)]
cubicspline(n=2, xn=x_vec, an=a_vec, fpo=df(0), fpn=df(2))


# Codes Part 2

import math

def S0(x):
    return -0.83907*x-0.0097306*x**2-0.12329*x**3

def S1(x):
    return -0.70605-0.44975*(x-1)+0.37959*(x-1)**2-0.013249*(x-1)**3

def f(t):
    return 1/2*(math.sin(10+t)-math.sin(10-t))

print(S0(0.3),S0(0.8),S1(1.5),S1(1.7))
print(f(0.3),f(0.8),f(1.5),f(1.7))
print(abs(S0(0.3)-f(0.3)),abs(S0(0.8)-f(0.8)),abs(S1(1.5)-f(1.5)),abs(S1(1.7)-f(1.7)))

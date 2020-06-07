import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

plt.figure('lin')
plt.clf()
plt.xlabel('sample points')
plt.title('linear function')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.xlabel('sample points')
plt.title('quadratric function')
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.clf()
plt.xlabel('sample points')
plt.title('cubic function')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.clf()
plt.xlabel('sample points')
plt.title('exponential function')
plt.plot(mySamples, myExponential)
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

# Basic plotting
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

# plot within set figures & adding labels
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

# plot with specific axis ranges
plt.figure('lin')
plt.clf()
plt.ylim(0,1000)
plt.title('Linear')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0,1000)
plt.title('Quadratic')
plt.plot(mySamples, myQuadratic)

#plot multiple plots, explicitly
#add legends to plots
plt.figure('lin quad')
plt.clf()
plt.title("linear vs Quadratic")
plt.plot(mySamples, myLinear, label = 'linear')
plt.plot(mySamples, myQuadratic, label = 'quadratic')
plt.legend(loc = 'upper left')
plt.figure('cube exp')
plt.clf()
plt.title("Cubic vs Exponential")
plt.plot(mySamples, myCubic, label = 'cubic')
plt.plot(mySamples, myExponential, label = 'exponential')
plt.legend()

#modify line appearances
plt.figure('lin quad')
plt.clf()
plt.title("linear vs Quadratic")
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.plot(mySamples, myQuadratic, 'ro', label = 'quadratic', linewidth = 3.0)
plt.legend(loc = 'upper left')
plt.figure('cube exp')
plt.clf()
plt.title("Cubic vs Exponential")
plt.plot(mySamples, myCubic, 'k^', label = 'cubic', linewidth = 4.0)
plt.plot(mySamples, myExponential, 'g--', label = 'exponential', linewidth = 5.0)
plt.legend()

#plot each function in subplots
plt.figure('lin quad')
plt.clf()
plt.subplot(211)    #("number rows", "number columns", "location of subplot")
plt.ylim(0,900)
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.legend()
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic, 'ro', label = 'quadratic', linewidth = 3.0)
plt.legend()
plt.title("linear vs Quadratic")

plt.figure('cube exp')
plt.clf()
plt.subplot(121)
plt.ylim(0,14000)
plt.plot(mySamples, myCubic, 'k^', label = 'cubic', linewidth = 4.0)
plt.subplot(122)
plt.ylim(0,14000)
plt.legend()
plt.plot(mySamples, myExponential, 'g--', label = 'exponential', linewidth = 5.0)
plt.legend()
plt.title("Cubic vs Exponential")

#plot with different scales, linear first (standard) then logarithmic scale
plt.figure('lin quad')
plt.clf()
plt.title("linear vs Quadratic")
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.plot(mySamples, myQuadratic, 'ro', label = 'quadratic', linewidth = 3.0)
plt.legend()
plt.figure('cube exp')
plt.clf()
plt.title("Cubic vs Exponential")
plt.plot(mySamples, myCubic, 'k^', label = 'cubic', linewidth = 4.0)
plt.plot(mySamples, myExponential, 'g--', label = 'exponential', linewidth = 5.0)
plt.yscale('log')
plt.legend()


#example
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate)+monthly]
    return base, savings

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals,
                label = 'retire: $'+str(monthly))
        plt.legend(loc = 'upper left')

displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40*12)

def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals,
                label = 'retire: $'+str(month)+': '+str(int(rate*100))+"%")
        plt.legend(loc = 'upper left')

displayRetireWRates(800, [.03, .05, .07], 40*12)

def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r','b','g','k']
    rateLabels = ['-',':','--']
    for i in  range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals,
                    (monthLabel+rateLabel), linewidth = 1.0,
                    label = 'retire: $'+str(monthly)+': '+str(int(rate*100))+'%')
            plt.legend(loc = 'upper left')

displayRetireWMonthsAndRates([500,700,900,1100], [.03,.05,.07], 40*12)
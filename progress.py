import pylab
from datetime import datetime

X = []
A = []
N = []

t0 = None
tot = 0
with open("progress.log") as f:
    for line in f:
        tot += 1
        n, t = line.split()
        t = datetime.strptime(t, '%Y-%m-%d.%H:%M')
        if t0:
            dt = (t - t0)
            dt = dt.days + dt.seconds/86400.0
            ave = float(tot)/dt
            X.append(dt)
            A.append(ave)
            N.append(tot+84)
        else:
            t0 = t

# Plot:
pylab.figure(0)

# Average problems per day:
pylab.plot(X, A, 'go--')
pylab.show()

# Total problems vs days:
pylab.plot(X, N, 'bo--')
pylab.plot([1,365], [85, 460], 'ro--')
pylab.xlim([0,100])
pylab.ylim([50,200])
pylab.show()

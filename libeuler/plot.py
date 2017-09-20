# Standard libs:
import sys
import matplotlib.pyplot as plt
sys.path.append("..")

# Read data:
from p357.p357 import benchmarks

# Create plot::
plt.figure(0, (12,7))

# Add data:
for where, results in benchmarks.items():
    for fun, data in results.items():
        X, Y = [], []
        for line in data:
            x, _, y = line
            X.append(x)
            Y.append(y)
        
        label = "{f} @ {w}".format(f=fun, w=where)
        plt.plot(X, Y, label=label)

# Configure and show plot:
legend = plt.legend(loc='upper left', shadow=True)
plt.show()

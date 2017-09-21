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
    for fun, fundata in results.items():
        X, Y = [], []
        if fundata.get("skip", False):
            continue

        for line in fundata.get("data", []):
            x, _, y = line
            X.append(x)
            Y.append(y)
        
        label = "{f} @ {w}".format(f=fun, w=where)
        plt.loglog(X, Y, label=label)

# Configure and show plot:
legend = plt.legend(loc='upper left', shadow=True)
plt.show()

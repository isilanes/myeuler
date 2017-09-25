# Standard libs:
import sys
import importlib
import matplotlib.pyplot as plt
import argparse

# Functions:
def main():
    """Main plotting."""

    # Parse command-line arguments:
    opts = parse_args()

    # Read data:
    module_name = "{p}.{p}".format(p=opts.problem)
    try:
        problem = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print("Sorry, could not load problem {p}".format(p=opts.problem))
        exit()

    # Create plot::
    plt.figure(0, (12,7))

    # Add data:
    for where, results in problem.benchmarks.items():
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
    plt.xlabel("Problem size")
    plt.ylabel("Time (ms)")
    plt.show()

def parse_args(args=sys.argv[1:]):
    """Read and parse arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--problem",
            help="Which problem to plot. Default: p357.",
            default="p357")


    return parser.parse_args(args)



# Main:
if __name__ == "__main__":
    main()


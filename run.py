import sys
import random


if __name__ == "__main__":
    return_code = random.randint(0, 1)
    if return_code == 0:
        print("print1", file=sys.stdout)
        print("print2", file=sys.stdout)
    else:
        print("error1", file=sys.stderr)
        print("error2", file=sys.stderr)
    sys.exit(return_code)

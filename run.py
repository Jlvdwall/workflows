import sys
import random
import pathlib


if __name__ == "__main__":
    return_code = random.randint(0, 1)
    if return_code == 0:
        aws_response = (pathlib.Path(__file__).parent / "test.json").read_text()
        print(aws_response, file=sys.stdout)
    else:
        print("error1", file=sys.stderr)
        print("error2", file=sys.stderr)
    sys.exit(return_code)

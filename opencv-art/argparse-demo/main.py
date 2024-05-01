import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integers', type=int, nargs='+')
parser.add_argument('--sum', dest='op', action='store_const', const=sum, default=max)

args = parser.parse_args()
print(args.op(args.integers))
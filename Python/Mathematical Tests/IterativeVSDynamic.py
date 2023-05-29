import time
import argparse

parser = argparse.ArgumentParser(description="Input for Iteration of Fibonacci")

args = parser.add_argument('-l', '--length', type=int, required=True, metavar='')

args = parser.parse_args()

def IterativeFib(n):
    arr = [0,1]
    if n < 0:
        return -1
    if n == 0:
        print(arr[0])
    if n == 1:
        print(arr[1])
    for i in range(2,n):
        arr.append(arr[i-1]+arr[i-2])
        print(arr[i])

def main():
    IterativeFib(args.length)

if __name__ == '__main__':
    main()

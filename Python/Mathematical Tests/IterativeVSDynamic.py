import time

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
    IterativeFib(10)

if __name__ == '__name__':
    main()

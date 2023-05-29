# counter = 0
def recursive(i):
    print('i = ',i)
    if i == 0:
        print("Done")
        return i
    while i != 0:
        # counter = counter + 1
        recursive(i-1)
    # print("Recursion times used: ",counter)

if __name__ == '__main__':
    recursive(20)

import random
import time

def swap(a, b) : 
    return b, a

def sort(arr) :
    print(arr)
    for i in range(0, len(arr)) :
        tmp = i
        for j in range(i + 1, len(arr)) : 
            if arr[tmp] > arr[j] :
                tmp = j
        arr[i], arr[tmp] = swap(arr[i], arr[tmp])
    
    return arr

if __name__ == "__main__" : 

    start = time.time()

    arr = []
    arrlen = 1000

    for i in range(arrlen) : 
        n = random.randint(1, 10000000)
        arr.append(n)

    arr = sort(arr) 
    print(arr)

    print("Elapsed Time : {0}".format(round(time.time() - start, 2)))
    
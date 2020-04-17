if __name__ == '__main__':
    n = int(raw_input())
    arr = list(map(int, raw_input().split()))
    zes=max(arr)
    i=0
    while(i<n):
        if zes==max(arr):
            arr.remove(max(arr))
        i+=1
    print(max(arr))    


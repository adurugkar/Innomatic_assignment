# find the Runner-UP Score

def check(n,arr):
    arr = list(arr)
    arr.sort()
    lst = []
    for i in arr:
        if i < arr[n-1]:
            lst.append(i)
    t =len(lst)
    print(lst[t-1])      

if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    check(n,arr)
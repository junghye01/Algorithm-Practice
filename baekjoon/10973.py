import sys

def prev_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] <= arr[i + 1]: # 마지막 원소부터 탐색하면서 오름차순이 아닌 부분 찾음
        i -= 1
    if i >= 0:
        j = len(arr) - 1 # 맨 끝
        while arr[j] >= arr[i]: # 
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = arr[i+1:][::-1]

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

prev_permutation(lst)

if lst == sorted(lst,reverse=True):
    print(-1)

else:
    print(" ".join(map(str,lst)))


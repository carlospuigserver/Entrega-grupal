n=int(input())
array=list(map(int,input().split()))
total=0

for element in array:
    total+=element
    print(total)
import heapq

left = []
right = []

with open("input.txt", "r") as file:
    for line in file:
        leftnum = int(line.strip().split(" ")[0])
        rightnum = int(line.strip().split(" ")[-1])
        heapq.heappush(left, leftnum)
        heapq.heappush(right, rightnum)

result = 0

for i in range(1000):
    l = heapq.heappop(left)
    r = heapq.heappop(right)
    result = result + ( abs( r - l )  ) 
    
print(result)
counter = {}
result = 0
with open("input.txt", "r") as file:
    for line in file:
        leftnum = int(line.strip().split(" ")[0])
        counter[leftnum] = 0
    file.close()
with open("input.txt", "r") as file:
    for line in file:
        rightnum = int(line.strip().split(" ")[-1])
        if(rightnum in counter):
            counter[rightnum] = counter[rightnum] + 1
    file.close()
# print(counter)

for key in counter:
    if(not counter[key] == 0):
        result = result + (key * counter[key])

print(result)
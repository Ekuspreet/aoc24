import re

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
pattern_nums = r"\d{1,3}"
with open("input.txt", "r") as file:
    lines = file.read()
    file.close()
result = 0
lines = re.findall(pattern, lines)
mulfactor = 1
for line in lines:
    if line == "do()":
        mulfactor = 1
    elif line == "don't()":
        mulfactor = 0
    else:
        nums = re.findall(pattern_nums, line)
        result = result + int(nums[0]) * int(nums[1]) * mulfactor
print(result)
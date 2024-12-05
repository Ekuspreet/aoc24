import re

pattern = r"mul\(\d{1,3},\d{1,3}\)"
pattern_nums = r"\d{1,3}"
with open("input.txt", "r") as file:
    lines = file.read()
    file.close()
result = 0
lines = re.findall(pattern, lines)
for line in lines:
    nums = re.findall(pattern_nums, line)
    result += int(nums[0]) * int(nums[1])
print(result)
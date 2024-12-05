result = 0
def matchInDirection(i, j, di, dj, lines):
    matches = 0
    if lines[i + di][j + dj] == 'M'  and lines[i + 2*di][j + 2*dj] == 'A' and lines[i + 3*di][j + 3*dj] == 'S':
        matches = matches + 1
    return matches

# Matching XMAS in all directions
def countMatches(i, j, lines):
    matches = 0
    rows = len(lines)
    cols = len(lines[0])

    # Guard clauses for each direction
    if i - 3 >= 0:  # Upward
        matches += matchInDirection(i, j, -1, 0, lines)
    if i - 3 >= 0 and j - 3 >= 0:  # Upward-left 
        matches += matchInDirection(i, j, -1, -1, lines)
    if i - 3 >= 0 and j + 3 < cols:  # Upward-right 
        matches += matchInDirection(i, j, -1, 1, lines)
    if i + 3 < rows:  # Downward
        matches += matchInDirection(i, j, 1, 0, lines)
    if i + 3 < rows and j - 3 >= 0:  # Downward-left 
        matches += matchInDirection(i, j, 1, -1, lines)
    if i + 3 < rows and j + 3 < cols:  # Downward-right 
        matches += matchInDirection(i, j, 1, 1, lines)
    if j - 3 >= 0:  # Leftward
        matches += matchInDirection(i, j, 0, -1, lines)
    if j + 3 < cols:  # Rightward
        matches += matchInDirection(i, j, 0, 1, lines)

    return matches

with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    file.close()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'X':
                result = result + countMatches(i, j, lines)
                
print(result)
result = 0

def countMatches(i,j,lines):
   
    # Top Left and Bottom Right
    condition1 = (lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S') or \
                 (lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M')
    # Top Right and Bottom Left
    condition2 = (lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S') or \
                 (lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M')

    return condition1 and condition2

with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    file.close()
    for i in range(1,len(lines)-1):
        for j in range(1,len(lines[i])-1):
            if lines[i][j] == 'A':
                result = result + countMatches(i, j, lines)
print(result)
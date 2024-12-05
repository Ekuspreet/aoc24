
def isReportSafe(report):
    report = list(map(int, report))
    inc_flag = False
    dec_flag = False
    if(len(report) == 1):
        return True
    if(report[0] < report[1]):
        inc_flag = True
    else:
        dec_flag = True
    # print("Inc Flag : ", inc_flag , " Dec Flag : ", dec_flag)
    for value in range(len(report)-1):
        if(not((inc_flag and report[value] < report[value+1])  or (dec_flag and report[value] > report[value+1] ) ) ):
            # print("Reason : Not in order")
            return False
        if(not(abs(report[value] - report[value+1]) <= 3 )):
            # print("Reason : Not 3 apart")
            return False
    return True    
counter = 0
with open("input.txt", "r") as file:
    for line in file:
        report = line.strip().split(" ");
        counter = counter + isReportSafe(report)
print(counter)
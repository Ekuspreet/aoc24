
# def isReportSafe(report):
#     k = 1
#     report = list(map(int, report))
#     inc_flag = False
#     dec_flag = False
#     if(len(report) == 1):
#         return True
#     if(report[0] < report[1]):
#         inc_flag = True
#     else:
#         dec_flag = True
#     # print("Inc Flag : ", inc_flag , " Dec Flag : ", dec_flag)
#     for value in range(len(report)-1):
#         if(not((inc_flag and report[value] < report[value+1])  or (dec_flag and report[value] > report[value+1] ) ) ):
#             if (k==0):
#                 return False
#             k= k-1
#         if(not(abs(report[value] - report[value+1]) <= 3 )):
#             if(k==0):
#                 return False
#             k = k-1
#     return True
# 

# def isReportSafe(report):
#     report = list(map(int,report))
#     n = len(report)
#     safety_score = 0
#     for i in range(len(report)-1):
#         if(report[i] < report[i+1] and abs(report[i] - report[i+1]) <= 3):
#             safety_score = safety_score + 1
#         if(report[i] > report[i+1] and abs(report[i] - report[i+1]) <= 3):
#             safety_score = safety_score - 1
#         if(report[i] == report[i+1]):
#             safety_score = safety_score - 1
#     print(safety_score)
#     if(abs(safety_score) >= n-2):
#         return True
#     return False

def isReportSafe(report):
    if(len(report) < 3):
        print("True")
    else:
        print("False")
# 18 21 22 24 26 29 28
# 9 11 14 17 18 21 21 


counter = 0
with open("input.txt", "r") as file:
    for line in file:
        report = line.strip().split(" ");
        isReportSafe(report)
        # counter = counter + isReportSafe(report)
# print(counter)
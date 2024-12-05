def isReportSafe(report):
    report = list(map(int, report))
    if len(report) == 1:  # Single-level reports are always safe
        return True

    # Determine the trend of the sequence
    inc_flag = report[0] < report[1]
    for i in range(len(report) - 1):
        if not ((inc_flag and report[i] < report[i + 1]) or (not inc_flag and report[i] > report[i + 1])):
            return False  # Not in monotonic order
        if abs(report[i] - report[i + 1]) > 3:
            return False  # Difference exceeds the limit
    return True


def isReportSafeWithDampener(report):
    # If already safe, return True
    if isReportSafe(report):
        return True

    # Try removing each level and re-check
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove the i-th level
        if len(modified_report) < 2:  # No need to check single-element reports
            return True
        # Recalculate trend and check if modified report is safe
        if isReportSafe(modified_report):
            return True

    return False  # No way to make it safe


# Main logic
counter = 0
with open("input.txt", "r") as file:
    for line in file:
        report = line.strip().split(" ")
        if isReportSafeWithDampener(report):
            counter += 1

print(counter)


def compareVersion(version1: str, version2: str) -> int:
    temp1 = version1.split('.')
    temp2 = version2.split('.')
    sum1 = sum2 = 0
    for ch in temp1:
        sum1 += int(ch)
    for ch in temp2:
        sum2 += int(ch)
    if sum1 == sum2:
        return 0
    elif sum1 > sum2:
        return 1
    else:
        return -1


if __name__ == '__main__':
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    print(compareVersion(version1, version2))

def HighestThree(hightList):
    list1=hightList
    list1.sort()
    list1.reverse()
    x = list1[0:3]
    return x
print(f'The highest three buldings are = {HighestThree([1,2,3,4,1,100,30,5])}')
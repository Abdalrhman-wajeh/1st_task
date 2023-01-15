def duplictation(numList):
    numFoDubles = 0
    y=set(numList)
    if len(numList)>len(y):
        numFoDubles = len(numList)-len(y)
    
    return (numFoDubles)
my_list = [1,2,3,4,5,6,7,8,9]
print(f'Number fo duplication = {duplictation(my_list)}')

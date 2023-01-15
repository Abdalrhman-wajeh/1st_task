def NumOfOcurences(string,letter):
    ocurences = 0
    for x in string:
        if x == letter:
            ocurences += 1
    return ocurences
print(f'Number of ocurences = {NumOfOcurences("Abdalrhman wajeh","a")}')
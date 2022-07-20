def main():
    word = input('Enter word = ')
    full = len(word)
    half = (len(word)/ 2)
    firsthalf_symm = word[0:int(half)]
    firsthalf_pal = word[0:int(half)][::-1]
    if len(word) % 2 != 0:  # odd number of letters
        secondhalf_symm = word[int(half) + 1:full + 1]
        secondhalf_pal = word[int(half) + 1:full + 1]
        ifstatements(firsthalf_symm, secondhalf_symm, firsthalf_pal,secondhalf_pal)
    else:
        secondhalf_symm = word[int(half):full + 1]
        secondhalf_pal = word[int(half):full + 1]
        ifstatements(firsthalf_symm, secondhalf_symm, firsthalf_pal,secondhalf_pal)

def ifstatements(firsthalf_symm, secondhalf_symm,firsthalf_pal,secondhalf_pal):
    print(firsthalf_symm, secondhalf_symm, firsthalf_pal, secondhalf_pal)
    if firsthalf_symm == secondhalf_symm and firsthalf_pal != secondhalf_pal:
        print("The entered string is symmetrical and not a palindrome")
    elif firsthalf_pal == secondhalf_pal and firsthalf_symm != secondhalf_symm:
        print("The entered string is a palindrome and not symmetrical")
    elif firsthalf_symm == secondhalf_symm and firsthalf_pal == secondhalf_pal:
        print("The entered string is a palindrome and symmetrical")
    else:
        print("The entered string is not a palindrome nor symmetrical")

main()

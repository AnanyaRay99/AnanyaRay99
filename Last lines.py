def file():
    fileobj = open(r"C:\Users\anany\Downloads\words.txt")
    lines = []
    for line in fileobj:
        lines.append(line.strip())
# Last lines in a file
    x = int(input("Enter number of last words required: "))
    if x > int(len(lines)):
        print(f"Please enter a number less than or equal to {len(lines)}")
    elif x < 0:
        print(f"Please enter a number greater than or equal to 1")
    else:
        lastlines = lines[len(lines) - x: len(lines)+1]
        print(lastlines)

file()

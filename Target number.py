#[3, 5, -4, 8, 11, 1, -1, 6], target = 10
#[-1, 11]

l = [3, 5, -4, 8, 11, 1, -1, 6]
emptydict = {}
tgt = 10

print(emptydict)
def main():
    for x in l:
        if x not in emptydict:
            emptydict[tgt - x] = [x]
        else:
            print(x, tgt - x)
    print(emptydict)

# To find 7, 5, 14, 2, -1, 9, 11, 4.
# 3|7, 5|5, -4|14, 8|2, 11|(-1), 1|9, -1|11, 6|4
# 7, 5, 14, 2, -1, 9, 11
# 3, 5, -4, 8, 11, 1, -1

#[3, 5, -4, 8, 11, 1, -1, 6]
# 10-3 = 7, 10 - 5 = 5, 10-(-4) = 14, 10-8 = 2, 10-11 = -1, 10-1 = 9, 10-(-1) = 11
# 7:3,5:5,14:-4,2:8,-1:11,9:1,

# 7, 5, 14,
# 3, 5, -4,

# 3, 10-3 = 7
# 5, 10-5 = 5
# -4, 10+4 = 14
# 8, 10-8 = 2
# 11, 10-11= -1 <>
# 1, 10-1 = 9
# -1, 10-(-1)= 11
# 6, 10-6 = 4

if __name__ == '__main__': main()
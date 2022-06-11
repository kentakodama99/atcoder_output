import sys

S = input()
aski = [0] * 123

moji_f = [0] * 2
for s in S:
    text = ord(s)
    if 65 <= text <= 90 and not aski[text]:
        aski[text] += 1
        moji_f[0] = 1
    elif 97 <= text <= 122 and not aski[text]:
        aski[text] += 1
        moji_f[1] = 1
    else:
        print("No")
        sys.exit()
print("Yes" if sum(moji_f) == 2 else "No")

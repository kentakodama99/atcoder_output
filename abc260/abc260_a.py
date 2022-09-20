S = input()

if not S[0] == S[1]:
    if S[1] == S[2]: # abb
        print(S[0])
    elif S[0] == S[2]: # aba
        print(S[1])
    else: # abc
        print(S[0])
else:
    if not S[1] == S[2]: # aab
        print(S[2])
    else:
        print("-1") # aaa
A, B, C, D, E, F, X = map(int, input().split())
t = (A * (X // (A + C)) + min(A, X % (A + C))) * B
a = (D * (X // (D + F)) + min(D, X % (D + F))) * E

if t > a:
    print("Takahashi")
elif t < a:
    print("Aoki")
else:
    print("Draw")
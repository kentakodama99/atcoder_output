K = int(input())

h, m = divmod(K, 60)
print(str(21 + h) + ":" + str(m).zfill(2))
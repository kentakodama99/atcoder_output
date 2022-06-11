res_a = [str(i) for i in range(1, 100)]
res_b = [str(i * 100) for i in range(1, 100)]
res_c = [str(i * 10000) for i in range(1, 100)]

res = res_a + res_b + res_c

print(len(res))
print(" ".join(res))
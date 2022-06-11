S = input()

hasBoth = not S.islower() and not S.isupper()
hasDuplicate = len(set(S)) != len(S)

if hasBoth and not hasDuplicate:
  print('Yes')
else:
  print('No')
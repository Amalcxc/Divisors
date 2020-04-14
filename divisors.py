ask = int(input("choose a number: "))

listR = list(range(1,ask+1))

range = []

for i in listR:
  if ask % i == 0:
    range.append(i)

print(range)

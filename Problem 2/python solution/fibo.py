previousNumber, currentNumber = 0, 1
nextNumber = 1
sum = 0

while nextNumber <= 4000000:
  if nextNumber % 2 == 0:
    sum += nextNumber
  nextNumber = currentNumber + previousNumber
  previousNumber, currentNumber = currentNumber, nextNumber

print(sum)
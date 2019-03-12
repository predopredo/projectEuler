def findSum(initial, final, multiples):

  if initial < final:
    smaller, bigger = initial, final

  elif initial > final: 
    smaller, bigger = final, initial
  
  else:
    return "Please insert an interval between 2 different numbers"

  sum = 0

  if isinstance(multiples, list):
    multiplesString = "%s and %s" % (", ".join([str(i) for i in multiples[:-1]]), multiples[len(multiples)-1])
    for x in range(round(smaller), round(bigger)):
      checkIfSame = None
      for y in multiples:
        if x % y == 0 and not x == checkIfSame:
          sum += x
          checkIfSame = x
    return "The sum of all the multiples of %s between %s and %s is %s" % (multiplesString, initial, final, sum)

  else:
    for x in range(round(smaller), round(bigger)):
      if x % multiples == 0:
        sum += x
    return "The sum of all the multiples of %s between %s and %s is %s" % (multiples, initial, final, sum)

print(findSum(0, 1000, [3,5]))
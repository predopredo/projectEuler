def findSum(initial, final, multiples):
  
  if isinstance(multiples, list) and len(multiples) > 1:
    multiplesString = "%s and %s" % (", ".join([str(i) for i in multiples[:-1]]), multiples[len(multiples)-1])
  elif isinstance(multiples, list) and len(multiples) == 1:
    multiplesString = "%s" % (multiples[0])
  else:
    multiplesString = multiples

  if initial < final:
    smaller, bigger = initial, final

  elif initial > final: 
    smaller, bigger = final, initial
  
  else:
    return "Please insert an interval between 2 different numbers"

  result = 0

  if isinstance(multiples, list):
    for x in range(round(smaller), round(bigger)):
      checkIfSame = None
      for y in multiples:
        if x % y == 0 and not x == checkIfSame:
          result += x
          checkIfSame = x
  
  else:
    for x in range(round(smaller), round(bigger)):
      if x % multiples == 0:
        result += x

  if result > 0:
    return "The sum of all the multiples of %s between %s and %s is %s" % (multiplesString, initial, final, result) 
  else: 
    return "There are no multiples of %s between %s and %s" % (multiplesString, initial, final)

print(findSum(0, 1000, [3,5]))
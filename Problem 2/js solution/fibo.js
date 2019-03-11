let previousNumber = 0
let currentNumber = 1
let nextNumber = 1
let sum = 0

while (nextNumber <= 4000000) {
  if (nextNumber % 2 === 0) {
    sum += nextNumber
  }
  nextNumber = currentNumber + previousNumber
  previousNumber = currentNumber
  currentNumber = nextNumber
}

console.log(sum)
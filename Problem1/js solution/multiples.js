function findAnySum(initial, final, multiplesOf) {

    let multiplesOfArray = JSON.parse(`[${multiplesOf}]`)
  
    let textMultiples = multiplesOfArray.length > 1 ? `${multiplesOfArray.slice(0, (multiplesOfArray.length - 1)).join(', ')} e ${multiplesOfArray[multiplesOfArray.length - 1]}` : multiplesOfArray.join('')
  
    let result = 0
  
    if (initial < final) {
      var smaller = initial
      var bigger = final
    } else if (initial > final) {
      var smaller = final
      var bigger = initial
    } else {
        return 'Please insert an interval between 2 different numbers'
    }
  
    for (let current = Math.round(smaller); current < Math.round(bigger); current++) {
      let checkIfSame
      multiplesOfArray.forEach(multiple => {
        if (current % multiple === 0 && current != checkIfSame) {
          result += current;
          checkIfSame = current
        }
      })
    }
    if (result === 0) {
      return `There are no multiples of ${textMultiples} between ${initial} and ${final}`
    } else {
      return `Solution result: The sum of all multiples of ${textMultiples} between ${initial} and ${final} is ${result}`
    }
  }

  console.log(findAnySum(0, 1000, [3, 5]));
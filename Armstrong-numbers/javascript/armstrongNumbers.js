// # turn input number into an array
// # count array and save to variable
// # save number of the index as a variable to keep track of it
// # calculate the exponents 
// # add the answers together and return the total
// # loop through array from 0 to 999 to check for armstrong numbers within and output those numbers to an array

function isArmstrongNumber(num) {
    let exponentList = [];
    let numberOfDigits = num.toString().length;

    let sumOfExponentList = 0;
    let arr = num.toString().split('').map(Number);

    for(let i = 0; i < arr.length; i++) {
      exponentList.push(Math.pow(arr[i], numberOfDigits));
    }

    let sum = exponentList.reduce(function(a, b) {
      return a + b;
    }, 0);

    if (sum === num) {
      return true;
    } else {
      return false;
    }
  };

function findArmstrongNumbers(num1, num2) {
  let newArr = [];
  let newerArr = [];

  for(let i = num1; i <= num2; i++) {
    newArr.push(i);
  };

  for(let i = 0; i < newArr.length; i++) {
    if (isArmstrongNumber((i)) === true) {
      newerArr.push(newArr[i]);
    } 
  };

  return newerArr;

};



module.exports = {
  isArmstrongNumber: isArmstrongNumber,
  findArmstrongNumbers: findArmstrongNumbers
}

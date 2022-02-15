// Can you translate this driver code to unit tests?


const { isArmstrongNumber, findArmstrongNumbers } = require('./armstrongNumbers');
var shallowEqualArrays = require('shallow-equal/arrays');



function createArrayOfNum(maxValue) {
  return Array.apply(null, {length: maxValue}).map(Number.call, Number)
}

console.log(findArmstrongNumbers([0]),[0]);
console.log(findArmstrongNumbers(createArrayOfNum(0, 8)), [0, 1, 2, 3, 4, 5, 6, 7]);
console.log(findArmstrongNumbers(createArrayOfNum(0, 99)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
console.log(findArmstrongNumbers(createArrayOfNum(0, 999)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]);
// run `npm install shallow-equal --save` in this folder before you get started with this challenge
// Rewrite this in Unit Test



let sp = require("./stockPicker");
let shallowEqualArrays = require('shallow-equal/arrays');

test('Testing to see if returns an array', () => {
    expect(Array.isArray(sp.picker([17,3,6,9,15,8,6,1,10]))).toEqual(true)})

test('Testing for expected result', () => {
     expect(sp.picker([17,3,6,9,15,8,6,1,10])).toEqual([1,4])})

test('Testing for expected result', () => {
    expect(sp.picker([3,17,6,9,18,15,6,1,10])).toEqual([0,4])})
   
test('Testing for expected result', () => {
    expect(sp.picker([1,17,6,9,8,15,6,3,19])).toEqual([0,8])})
   
test('Testing for expected result', () => {
    expect(sp.picker([19,17,6,9,8,15,6,3,1])).toEqual([2,5])})



// console.log(shallowEqualArrays(sp.picker([17,3,6,9,15,8,6,1,10]) , [1, 4]))
// console.log(shallowEqualArrays(sp.picker([17,3,6,9,15,8,6,1,10]), [1,4]))
// console.log(shallowEqualArrays(sp.picker([3,17,6,9,18,15,6,1,10]), [0,4]))
// console.log(shallowEqualArrays(sp.picker([1,17,6,9,8,15,6,3,19]), [0,8]))
// console.log(shallowEqualArrays(sp.picker([19,17,6,9,8,15,6,3,1]), [2,5]))
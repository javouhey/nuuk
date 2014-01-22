/**
 @module powersof2

 Checks if a number is a power of 2
 */
function isPowerOfTwo(n) {
  if (n <= 0) {
    return false;
  } else {
    return (n & -n) === n;
  }   
}

module.exports = isPowerOfTwo;

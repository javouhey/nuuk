/**
 @module random number within a range.
         Used for shuffling.
 */
function randomInt(min, max) {
  return Math.floor(
           Math.random() * (max - min + 1) + min);
}

module.exports = randomInt;

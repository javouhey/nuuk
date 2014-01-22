var powers2 = require('./powersof2'),
    randomInt = require('./random');

var testdata = [-1, 0, 1, 2, 3, 4];
testdata.forEach(function(el) {
  console.log(el + ' is a power of 2 ? ' + powers2(el));
});

console.log(' ');

[1, 2, 3].forEach(function(a) {
  console.log(randomInt(0, 5) + ' in range [0, 5]');    
});

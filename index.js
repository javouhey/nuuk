var powers2 = require('./powersof2');

var testdata = [-1, 0, 1, 2, 3, 4];
testdata.forEach(function(el) {
  console.log(el + ' is a power of 2 ? ' + powers2(el));
});

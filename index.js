var powers2 = require('./powersof2'),
    randomInt = require('./random'),
    seqtrans = require('./seqtrans'), 
    pos = require('./bitposition'),
    fs  = require("fs");

var testdata = [-1, 0, 1, 2, 3, 4];
testdata.forEach(function(el) {
  console.log(el + ' is a power of 2 ? ' + powers2(el));
});

console.log(' ');

[1, 2, 3].forEach(function(a) {
  console.log(randomInt(0, 5) + ' in range [0, 5]');    
});

// ------ sequence transformation -----

var filename = "./seqtrans/seq.data";
fs.readFileSync(filename).toString().split('\n').forEach(function (line) {
  if (line !== "") {
    var parts = line.split(' ');
    seqtrans.verify(parts[0], parts[1]);
  }
});

// ----- bit position -----

filename = "./bitposition/test.dat";
fs.readFileSync(filename).toString().split('\n').forEach(function (line) {
  if (line !== "") {
    var parts = line.split(',');
    pos.checkPositions(parts[0], parts[1], parts[2]);
  }
});


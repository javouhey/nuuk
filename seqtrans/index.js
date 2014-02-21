var Util = Object.create({});

var m = {
  '1': '(A+?|B+?)',
  '0': '(A+?)'
}

function compress_zeroes(a) {
  if (a) {
    result = '';
    var zeroes = false; 
    var ones = false;
    for (var o=0; o < a.length; o++) {
       var ch = a.charAt(o);

       switch(ch) {
       case '0':
           if (!zeroes) {
               zeroes = true;
               ones = false;
               result += '0';
           } 
           break;

       case '1':
           if (!ones) {
               ones = true;
               zeroes = false;
               result += '1';
           }
           break;

       default:
           return a; // only recognize characters in the set {0, 1}
       }
    }
    return result;

  } else {

    return a;
  }
}

function convertToRegex(str) {
  var h = compress_zeroes(str);
  //console.log("***** " + h);
  var pattern = '^';
  for (var o=0; o < h.length; o++) {
    pattern += m[h.charAt(o)];
  }
  //pattern += '$';
  //console.log(pattern);
  return new RegExp(pattern);
};

/**
 * @returns true if the regex built
 *          with 'left' matches 'right' 
 *          completely
 */
Util.verify = function(left, right) {
  var regex = convertToRegex(left);
  var result = regex.exec(right);
  //console.log(result);
  if (result === null) {
     return false; 
  } else {
     if (result[0] === right) {
         return true;
     } else {
         return false;
     }
  }
}

module.exports = Util;

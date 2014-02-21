/**
 * 0 -> A+
 * 1 -> A+ | B+
 */

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

   var pattern = '^';
   for (var o=0; o < h.length; o++) {
       pattern += m[h.charAt(o)];
   }
   //pattern += '$';
   console.log(pattern);
   return new RegExp(pattern);
};

var i = '1010';

console.log(i);
var regex = convertToRegex(i);
console.log(regex.exec("AAAAABBBBAAAA"));
console.log(regex.exec("ggghAAAAABBBBAAAA"));


regex = convertToRegex('01110110000010001011010100100011100001000100100010111110100111000000100000');

console.log(regex.exec('BAAABAAAAABBAABAAAAAABABAABBABAAABAAABBAABAABAAAABABAAAAAABBBBBABBBABBABAB'));

regex = convertToRegex('111110010010010000100111001101100011011011111110100110110');

var result = regex.exec('BBBBBBBBAAABBBBBAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBAAAAAAAAAAAAAAAAAAAABBBBBBAAAABBAAAAAAAAAABBAAAAAAAABBBBBBAAAAAAAA');
console.log(result);
console.log(result.input === result[0]);


var f = '111110010010010000100111001101100011011011111110100110110';

console.log(compress_zeroes(f));
console.log(f);


console.log('0111110000011100100101101011010101101100111111000111100010100011110010011111110100100110011100110011111110000010001100111101000100110000011');
regex = convertToRegex('0111110000011100100101101011010101101100111111000111100010100011110010011111110100100110011100110011111110000010001100111101000100110000011');

console.log('input=' + 'AABBABBBABBBBAAAAABAABBABAABAAAAABBAABAAAAABAABBABABABBBABBBBBABBBBBBAABBBBBBBBBABBBBBABBABBAABABABBBBABABBBABAABAABAAABBABABBBBBBBBABABBBA');
var result2 = regex.exec('AABBABBBABBBBAAAAABAABBABAABAAAAABBAABAAAAABAABBABABABBBABBBBBABBBBBBAABBBBBBBBBABBBBBABBABBAABABABBBBABABBBABAABAABAAABBABABBBBBBBBABABBBA');
console.log(result2);

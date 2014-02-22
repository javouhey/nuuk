var Util = {};

Util.checkPositions = function(target, pos1, pos2) {
    anumber = parseInt(target, 10);
    pos1 = parseInt(pos1, 10); 
    pos2 = parseInt(pos2, 10); 

    astr = anumber.toString(2);
    //console.log(astr + ':{' + pos1 + ', ' + pos2 + '}');

    astr = astr.split('').reverse().join('')
    if (astr.charAt(pos1-1) === astr.charAt(pos2-1)) {
       return 'true';
    } else {
       return 'false';
    } 
}

module.exports = Util;

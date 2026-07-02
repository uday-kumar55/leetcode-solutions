/**
 * @param {string} s
 * @return {number}
 */
var reverseDegree = function(s) {
    let sum = 0;
    for(let i=0;i<s.length;i++){
        let n =123 - s.charCodeAt(i) 
        sum+=n *(i+1)
    }
    return sum
};
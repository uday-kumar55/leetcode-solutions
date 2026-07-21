/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    target.sort((a, b) => a - b);
    let a = arr.sort((a,b)=>a-b);
    let i = 0;
    let j = 0;
    while (i <a.length && j<arr.length){
        if(target[i]!==a[j]){
            return false
        }
        i++
        j++
    }
    return true
};
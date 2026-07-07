/**
 * @param {number} n
 * @return {number}
 */
var sumAndMultiply = function(n) {
    let x =0;
    let sum =0;
    let place = 1;
    while(n>0){
        let digits = n%10
        if(digits!==0){
            sum+=digits;
            x+=digits*place
            place*=10
        }
        n=Math.floor(n/10)
    }
    return sum*x
};
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    let output = {}
    for(let i=0;i<nums.length;i++){
        let ch = nums[i]
        output[ch] = (output[ch]||0)+1
    }
    let n =[]
    for(let key in output){
        if(output[key]===1){
            n.push(Number(key))
        }
    } 
    let sum =0
    for(let i=0;i<n.length;i++){
        sum= sum+n[i]
    }
    return sum
    
                
};
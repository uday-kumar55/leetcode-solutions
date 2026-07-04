/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    let output ={}
    let output2 = []
    for(let i = 0;i<nums.length;i++){
        let ch = nums[i];
        output[ch] = (output[ch]||0)+1
    }
    for(let key in output){
        if(output[key]===1){
            output2.push(Number(key))
        }
    }
    return output2
};
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let max = -Infinity;
    let secondmax = -Infinity;
    for(let i=0;i<nums.length;i++){
        if(max<nums[i]){
            secondmax = max;
            max = nums[i]
        }else if(secondmax<nums[i]){
            secondmax =nums[i]
        }
    }
    return (max-1)*(secondmax-1)
};
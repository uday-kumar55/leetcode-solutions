/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let n = nums.length
    for(let i=0;i<nums.length;i++){
        if(nums[i]>=target){
            return i
        }
    }
    return n
};
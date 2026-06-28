/**
 * @param {number[]} nums
 * @return {number[]}
 */
var concatWithReverse = function(nums) {
    let reverse = []
    for(let i=0;i<nums.length;i++){
        reverse.push(nums[i])
    }
    for(let i =nums.length-1;i>=0;i--){
        reverse.push(nums[i])
    }
    return reverse
};
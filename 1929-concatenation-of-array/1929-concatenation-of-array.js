/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let n = nums.length
    let arr = new Array((n*2));
    for(let i =0;i<nums.length;i++){
        arr[i] = nums[i]
        arr[n+i] = nums[i]
    }
    return arr
};
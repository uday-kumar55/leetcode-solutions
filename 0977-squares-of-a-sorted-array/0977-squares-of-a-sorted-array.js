/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let a =[];
    for(let i=0;i<nums.length;i++){
        a[i] = nums[i]**2;
    }
    a.sort((a,b)=> a-b);
    return a
};
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMiddleElementUnique = function(nums) {
    let n = Math.floor(nums.length/2)
    let mid = nums[n]
    for(let i =0;i<nums.length;i++){
        if(i!==n&&mid===nums[i]){
            return false
        }
        
    }
    return true
};
/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
   let max =nums[0];
   for(let i=0;i<nums.length;i++){
    if(max < nums[i]){
        max = nums[i];
    }
   } 
   for(let i=0;i<nums.length;i++){
    if(max === nums[i]){
        return i;
    }
}
};
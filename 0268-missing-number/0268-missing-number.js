/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
    let output = 0;
    for (let i = 0; i <= nums.length; i++) {
        output = output ^ i
    }
    for (let i = 0; i< nums.length; i++) {
        output ^= nums[i]
    }
    return output
};
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let arr = [];
    let i =0
    while(i<nums2.length){
        if(nums1.includes(nums2[i])&&!arr.includes(nums2[i])){
            arr.push(nums2[i])
        }
        i++
    }
    return arr
};
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  let x ={}
  for(let i=0;i<nums.length;i++){
    let ch = nums[i]
    x[ch]=(x[ch]||0)+1

  }
  let output=0
  for(let key in x){
    if(x[key]===1){
        output =  (Number(key))
    }
  }
  return output
};
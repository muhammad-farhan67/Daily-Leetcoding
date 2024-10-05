class Solution {
    public int findNumbers(int[] nums) {
      int  count = 0;
    for (int i = 0; i < nums.length ; i++)
    {   if (nums[i] < 0)
         {
            nums[i] *= -1;
         }
        int totaldigits = (int)Math.log10(nums[i])+1;
        if (totaldigits % 2 == 0)
        {
            count++;
        }

    }
    return count;

        
    }
    
}
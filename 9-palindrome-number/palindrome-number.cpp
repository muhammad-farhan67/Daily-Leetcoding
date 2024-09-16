class Solution {
public:
    bool isPalindrome(int x) {
        int dup = x;
        int revnum = 0;
        if (x < 0)
          return false;
        while (x != 0) 
        {  
            int ld = x % 10;
            if((revnum > INT_MAX/10 )|| (revnum < INT_MIN/10))
            {
                return false;
            }
            revnum = (revnum * 10) + ld;
            x /= 10;
             
        }
         
         if (dup == revnum) 
            return true;
         else
           return false;
         
    }
};
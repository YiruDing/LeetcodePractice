// https://www.youtube.com/watch?v=gVUrDV4tZfY

class Solution {
    public int getSum(int a, int b) {
      
        while(b != 0){
            int temp = (a & b) <<1;
            // if a =1 and b =1
            // shift it to the left by one
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}

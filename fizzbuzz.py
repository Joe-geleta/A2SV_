class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            ap = ""
            if i%3==0:
                ap += "Fizz"
            if i%5==0:
                ap += "Buzz"
            if i%3!=0 and i%5!=0:
                ap = str(i)
            ans.append(ap)
        return ans
                

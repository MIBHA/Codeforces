import sys

class Solution:
    def solve(self):

        line1= sys.stdin.readline()
        if not line1: return
        t= int(line1)

        for _ in range(t):
            n= int(sys.stdin.readline())
            
            original= n
            k= 1
            d= 2

            while d* d<= n:
                if n % d== 0:
                    k= k*d

                    while n% d==0:
                        n= n//d

                d+= 1

            if n> 1:
                k= k*n

            print(k)

if __name__ == "__main__":
    Solution().solve()
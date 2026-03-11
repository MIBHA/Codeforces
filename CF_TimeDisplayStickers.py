import sys

class Solution:
    def solve(self):
        try:
            line1= sys.stdin.readline().strip()
            if not line1: return
            t= int(line1)
            
            line2= sys.stdin.readline().strip()
            if not line2: return
            n= int(line2)
            
            for _ in range(t):
                line3= sys.stdin.readline().strip().replace("{",'').replace("}",'').replace(",",'')
                if not line3: break
                s= line3
                
                cnt = [0]*10
                for c in s:
                    if c.isdigit():
                        cnt[int(c)] += 1

                ans = 0
                while True:
                    # Pick H1 (0-2)
                    h1 = -1
                    for d in [2, 1, 0]:
                        if cnt[d] > 0:
                            if d == 2:
                                cnt[d] -= 1
                                if any(cnt[x] > 0 for x in range(4)):
                                    h1 = d
                                    break
                                cnt[d] += 1
                            else:
                                h1 = d
                                cnt[d] -= 1
                                break
                    if h1 == -1: break

                    # Pick H2 (0-3 if h1 == 2, else 0-9)
                    h2 = -1
                    max_h2 = 3 if h1 == 2 else 9
                    for d in range(max_h2, -1, -1):
                        if cnt[d] > 0:
                            h2 = d
                            cnt[d] -= 1
                            break
                    if h2 == -1: break

                    # Pick M1 (0-5)
                    m1 = -1
                    for d in range(5, -1, -1):
                        if cnt[d] > 0:
                            m1 = d
                            cnt[d] -= 1
                            break
                    if m1 == -1: break

                    # Pick M2 (0-9)
                    m2 = -1
                    for d in range(9, -1, -1):
                        if cnt[d] > 0:
                            m2 = d
                            cnt[d] -= 1
                            break
                    if m2 == -1: break

                    ans += 1

                print(ans)

        except EOFError:
            return
        except ValueError:
            return
        except Exception as e:
            print(e)
            return

if __name__ == "__main__":
    Solution().solve()

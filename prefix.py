class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        ans = 0
        pre = [0]*n
        m = 10**9+7
        for i, vis in enumerate(nextVisit):
            if i+1>=n:
                break
            tmp = (2+pre[i] - ( pre[vis]))%m
            ans = (ans+tmp)%m
            pre[i+1] = ans%m
            # tmp = (m+2+pre[i]-(0 if vis==0 else pre[vis]))%m
            # ans = (ans+tmp)%m
            # pre[i+1] = ans

        return ans%m

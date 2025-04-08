class RecentCounter:

    def __init__(self):
        self.calls = []
        

    def ping(self, t: int) -> int:
        self.calls.append(t)
        count = 0
        for i in self.calls[::-1]:
            if i <= t :
                count += 1
            else:
                break
        return count
        


obj = RecentCounter()
print(obj.ping(10))
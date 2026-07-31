class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key] = self.hashmap.get(key, [])
        self.hashmap[key].append([timestamp, value])
    
    def get(self, key: str, timestamp: int) -> str:
        logs = self.hashmap.get(key, [])
        i = 0
        j = len(logs) - 1

        value = ""
        
        while i <= j:
            
            if i == j:
                if logs[i][0] <= timestamp:
                    value = logs[i][1]
                break

            mid = (i+j)//2
            if logs[mid][0] <= timestamp and logs[mid+1][0] > timestamp:
                value = logs[mid][1]
                break
            elif logs[mid][0] <= timestamp:
                i = mid + 1
            else:
                j = mid - 1

            
        
        return value
        

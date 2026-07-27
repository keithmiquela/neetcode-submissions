class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.dictionary.get(key):
            self.dictionary[key].append([timestamp, value])
        else:
            self.dictionary[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if not self.dictionary.get(key):
            return ""
        else:
            timemap = self.dictionary.get(key)
            target = timestamp

            if timemap[0][0] > timestamp:
                return ""
            
            def split(low, high):
                mid = math.ceil((high-low)/2 + low)
                curr_time = timemap[mid][0]
                curr_val = timemap[mid][1]
                if high == low:
                    return curr_val

                if curr_time == timestamp:
                    return curr_val
                elif curr_time > timestamp:
                    return split(low, mid-1)
                else:
                    return split(mid, high)
            return split(0, len(timemap)-1)

        

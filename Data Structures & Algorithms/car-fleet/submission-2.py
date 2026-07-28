class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # keep track of fleets
        # sorting by position increasing
        # start at 0, push to stack
        # next car, will it reach before previous car
        # if not, then pop stack until previous car reaches position after current
        # push to stack

        # car fleets = len of stack

        car_stack = []
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars = sorted(cars)
        def findTravelTime(position, speed):
            return (target - position)/speed

        for car in cars:
            if not car_stack:
                car_stack.append(car)
                continue
            prev_pos = car_stack[-1][0]
            prev_speed = car_stack[-1][1]
            prev_time = findTravelTime(prev_pos, prev_speed)

            pos = car[0]
            speed = car[1]
            time = findTravelTime(pos, speed)

            while time >= prev_time:
                car_stack.pop()
                if not car_stack:
                    break
                
                prev_pos = car_stack[-1][0]
                prev_speed = car_stack[-1][1]
                prev_time = findTravelTime(prev_pos, prev_speed)

            car_stack.append(car)

        return len(car_stack)

            
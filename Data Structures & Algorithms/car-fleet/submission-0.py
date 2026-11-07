class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        statuses = []
        for i in range(len(position)):
            car = [position[i], speed[i]]
            statuses.append(car)
        statuses.sort(key=lambda x: x[0], reverse=True)
        fleets = 0
        last_time = 0
        for position, speed in statuses:
            time = (target - position) / speed
            if time > last_time:
                fleets += 1
                last_time = time
        return fleets

        

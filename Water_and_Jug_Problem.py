class Solution:
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        if jug1Capacity +jug2Capacity < targetCapacity:
            return False
        if jug1Capacity == 0 or jug2Capacity == 0:
            return targetCapacity == 0 or jug1Capacity + jug2Capacity == targetCapacity
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0

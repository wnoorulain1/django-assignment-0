#Given a circular list of gas stations, where we can go from a station i to the station i + 1, and the last one goes back to the first one, find the index of the station from where we start to be able to traverse all the stations and go back to the initial one without running out of gas


def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1  # Not enough gas overall
    
    total = 0
    start = 0
    tank = 0
    
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:  # Can't reach next station from here
            start = i + 1
            tank = 0
    
    return start


# Example usage:
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(can_complete_circuit(gas, cost)) 

# we are given some lightbulbs numbered one to n. initially all the lightbulbs are turned off.

# when a bulb is turned on and all the bulbs to the left of a bulb are turned on. That bulb are turned on. That bulb
# turns blue our goal is to return the moment when all the bulbs turned on are turned blue. we are given an array in
# which the bulbs are turned on

def brute_force_solution(order: list) -> int:
    counter = 0
    for i in range(len(order)):
        bulb = abs(order[i])
        order[bulb - 1] = order[bulb - 1] * -1
        on_bulbs = 0
        for j in range(i + 1):
            if order[j] < 0:
                on_bulbs += 1
        if on_bulbs == i + 1:
            counter += 1
    return counter


import time


def solution(bridge_length, weight, truck_weights):
    waiting = truck_weights[::-1]
    passed = []
    passing = [0] * bridge_length
    # time = 0, passing = [0, 0, ..., 0, 0]   <--- waiting = [7,4,5,6]
    # time = 1, passing = [0, 0, ..., 0, 7]   <--- waiting = [4,5,6]
    # time = 2, passing = [0, 0, ..., 7, 4]   <--- waiting = [5,6]
    time = 0

    while len(truck_weights) > len(passed):
        if passing[0] != 0:
            passed.append(passing[0])
        passing.remove(passing[0])

        if waiting and sum(passing, waiting[0]) <= weight:
            passing.append(waiting.pop())
        else:
            passing.append(0)

        time += 1

    return time


# pass
def solution_rev(bridge_length, weight, truck_weights):
    passing = [0] * bridge_length
    time = 0

    # 매 주기마다 무조건 앞 요소 제거, 들어갈 요소 있으면 추가
    # 다 지나가면 len(passing) == 0
    while len(passing):
        passing.pop(0)

        if truck_weights:
            if sum(passing, truck_weights[0]) <= weight:
                passing.append(truck_weights.pop(0))
            else:
                passing.append(0)

        time += 1

    return time


if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]

    print(solution(bridge_length, weight, truck_weights))
    print(solution_rev(bridge_length, weight, truck_weights))

    bridge_length = 100
    weight = 100
    truck_weights = [10]

    print(solution(bridge_length, weight, truck_weights))
    print(solution_rev(bridge_length, weight, truck_weights))

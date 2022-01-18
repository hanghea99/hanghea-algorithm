# coding=utf-8
# 739. Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days
# you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


# [73, 74, 75, 71, 69, 72, 76, 73]
# temp = [(0, 1), (1, 2), (2, 6), (3, 5), (4, 5), (5, 6), (6, 6), (7, 7)]
# result = list(map(lambda x:x[1]-x[0], temp))

# result = list(가장 가까운 큰 값의 인덱스 - 현재 가리키고 있는 값 인덱스)
# list.index(val) -> 리스트에 중복된 값이 있을 경우, 첫번째 인덱스만 리턴
# dict -> key값 배정을 위해 for문을 돌려야됨
# enumerate -> for 구현없이 인덱스, 값 보존 가능

# 무식한 방법 -- 어찌되었든 이중 for문으로 timeout
def dailyTemperatures(temperatures):
    temps = list(enumerate(temperatures))
    result_list = [[index, 0] for index in range(len(temps))]

    for index, val in temps:
        if index == len(temps)-1:
            result_list[index][1] = index
        # for pair_index, pair_val in temps[index+1:]:
        #     if pair_val > val:
        #         result_list[index][1] = pair_index
        #         break
        i = 0
        while len(temps[index+1:]):
            pair_index = temps[index+1+i][0]
            pair_val = temps[index+1+i][1]
            if pair_val > val:
                result_list[index][1] = pair_index
                break
            i += 1
        if result_list[index][1] == 0:
            result_list[index][1] = index

    return list(map(lambda x:x[1]-x[0], result_list))

# 무식한 방법 : 거꾸로 세기 -- 1120ms (faster than 99%)
def dailyTemperatures_example0(temperatures):
    max = float('-inf')
    result = [0] * len(temperatures)

    for i in range(len(temperatures), -1, -1):
        temp_val = temperatures[i]
        if max <= temp_val:
            max = temp_val
        else:
            days = 1
            while temperatures[i+days] <= temp_val:
                days += result[i+days]
            result[i] = days
    return result

# 모범 답안 -- 1760ms (faster than 20%)
# 크지 않으면 index_stack에 잠시 index 저장
def dailyTemperatures_example1(temperatures):
    answer = [0] * len(temperatures)
    index_stack = []
    for index, value in enumerate(temperatures):
        while index_stack and value > temperatures[index_stack[-1]]:
            last_index = index_stack.pop()
            answer[last_index] = index - last_index
        index_stack.append(index)
    return answer

if __name__ == "__main__":
    # Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print("input >>> ", temperatures)
    print("output >>> ", dailyTemperatures(temperatures))

    # Input: temperatures = [30, 40, 50, 60]
    # Output: [1, 1, 1, 0]
    temperatures = [30, 40, 50, 60]
    print("input >>> ", temperatures)
    print("output >>> ", dailyTemperatures(temperatures))

    # Input: temperatures = [30, 60, 90]
    # Output: [1, 1, 0]
    temperatures = [30, 60, 90]
    print("input >>> ", temperatures)
    print("output >>> ", dailyTemperatures(temperatures))
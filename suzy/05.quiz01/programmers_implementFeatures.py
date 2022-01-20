# pass
def solution(progresses, speeds):
    progresses = progresses[::-1]
    speeds = speeds[::-1]
    completed = []

    while progresses:
        progresses = [progress + speed for progress, speed in zip(progresses, speeds)]
        completed_num = 0
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            completed_num += 1
        if completed_num > 0:
            completed.append(completed_num)

    return completed

# 모범답안
def solution_example(progresses, speeds):
    memo = []

    for progress, speed in zip(progresses, speeds):

        # 각 단계들이 완료될때까지 남은 시간
        # math.ceil((100-progress)//speed)과 같음
        left_days = -((progress - 100) // speed)

        # 메모에 앞 단계부터 [남은 날, 완료 갯수=1] 기록
        # 메모에 아직 안 적었거나, 다음 단계의 남은 날 > 앞 단계의 남은 날 -> 다음 단계의 [남은 날, 완료 갯수] 기록
        # 다음 단계의 남은 날 < 앞 단계의 남은 날 -> 앞 단계 완료 갯수 + 1
        if len(memo) == 0 or memo[-1][0] < left_days:
            memo.append([left_days, 1])
        else:
            memo[-1][1] += 1

        print("progress >> ", progress)
        print("speed >> ", speed)
        print("left_days >> ", left_days)
        print("memo >> ", memo)
        print()

    # 완료 갯수 리스트만 리턴
    return [m[1] for m in memo]


if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]

    print(solution(progresses, speeds))
    print(solution_example(progresses, speeds))
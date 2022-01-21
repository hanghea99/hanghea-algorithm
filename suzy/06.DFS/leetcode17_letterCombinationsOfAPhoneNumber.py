def lettersCombinations(digits):

    num_dict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    def dfs(key, words):
        if len(words) == len(digits):
            result.append(words)
            return

        for i in range(key, len(digits)):
            for j in num_dict[digits[i]]:
                dfs(i+1, words+j)

    result = []
    dfs(0, "")

    return result


if __name__ == "__main__":
    digits = "23"
    print(lettersCombinations(digits))
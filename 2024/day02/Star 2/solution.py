import os


class Puzzle:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.input_file_path = self._get_input_file_path()
        self.data = self._read_and_parse_input()

    def _get_input_file_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, self.input_file_name)

    def _read_and_parse_input(self):
        with open(self.input_file_path, "r") as file:
            data = file.read().strip().split("\n")
            return [list(map(int, line.split())) for line in data]

    def _is_ascending(self, num1, num2):
        return num2 > num1

    def _is_within_limit(self, num1, num2):
        return 1 <= abs(num1 - num2) <= 3

    def solveReport(self, report):
        isAscending = self._is_ascending(report[0], report[1])
        unsafe = False
        unsafeIndex = -1
        if isAscending:
            for n in range(len(report) - 1):
                if not (report[n] < report[n+1] and self._is_within_limit(report[n], report[n+1])):
                    unsafe = True
                    unsafeIndex = n
                    break
        else:
            for n in range(len(report) - 1):
                if not (report[n] > report[n+1] and self._is_within_limit(report[n], report[n+1])):
                    unsafe = True
                    unsafeIndex = n
                    break
        return unsafe, unsafeIndex

    def solve(self):
        safeCount = 0
        for report in self.data:
            unsafe, unsafeIndex = self.solveReport(report)
            if not unsafe:
                safeCount += 1
            else:
                # remove element n and retry solveReport with new array
                report.pop(unsafeIndex)
                unsafe, unsafeIndex = self.solveReport(report)
                if not unsafe:
                    safeCount += 1

        return safeCount


if __name__ == "__main__":
    testPuzzle = Puzzle("custom-test1.txt")
    print("total: ", testPuzzle.solve())

    realPuzzle = Puzzle("input.txt")
    print(realPuzzle.solve())

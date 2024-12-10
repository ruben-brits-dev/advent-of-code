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

    def check_report_safety(self, report):
        is_ascending = self._is_ascending(report[0], report[1])
        direction = 1 if is_ascending else -1

        for i in range(len(report) - 1):
            if not (direction * report[i] < direction * report[i + 1] and self._is_within_limit(report[i], report[i + 1])):
                return True, i

        return False, -1

    def is_safe_after_removal(self, report, index_to_remove):
        new_report = report[:index_to_remove] + report[index_to_remove + 1:]
        is_unsafe, _ = self.check_report_safety(new_report)
        return not is_unsafe

    def solve(self):
        safe_count = 0
        for report in self.data:
            is_unsafe, problem_index = self.check_report_safety(report)

            if not is_unsafe:
                safe_count += 1
            else:
                is_safe = False
                if problem_index > 0 and self.is_safe_after_removal(report, problem_index - 1):
                    is_safe = True
                elif self.is_safe_after_removal(report, problem_index):
                    is_safe = True
                elif problem_index + 1 < len(report) and self.is_safe_after_removal(report, problem_index + 1):
                    is_safe = True

                if is_safe:
                    safe_count += 1

        return safe_count


if __name__ == "__main__":
    testPuzzle = Puzzle("custom-test1.txt")
    print("total: ", testPuzzle.solve())

    realPuzzle = Puzzle("input.txt")
    print(realPuzzle.solve())

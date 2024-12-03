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

    @staticmethod
    def _get_occurences_in_col2(number, col2):
        return col2.count(number)

    def solve(self):
        col1, col2 = zip(*self.data)

        similarity = sum(x*self._get_occurences_in_col2(x, col2)
                         for x, y in zip(col1, col2))

        return similarity


if __name__ == "__main__":
    testPuzzle = Puzzle("custom-test1.txt")
    print("Total Distance:", testPuzzle.solve())

    realPuzzle = Puzzle("input.txt")
    print("Total Distance:", realPuzzle.solve())

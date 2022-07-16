"""
incorrectly formatted file for black pre-commit hook to fix with a few errors that a programmer would never ever make
"""

constant_value = 10


class wrong_class_name:
    """
    dummy class to demonstrate pylint
    """

    def __init__(self, input_value):
        """required init"""
        self.input_value = input_value

    def SquareInputs(self):
        """

        Args:
            input_value: some

        Returns:

        """
        input_value = self.input_value ^ 2

        return input_value


if __name__ == "__main__":
    test = wrong_class_name(10)
    print(test.SquareInputs())

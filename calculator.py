class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    @staticmethod
    def add(x, y):
        """
        Add two numbers.

        :param x: First number
        :param y: Second number
        :return: Sum of x and y
        """
        return x + y

    @staticmethod
    def subtract(x, y):
        """
        Subtract two numbers.

        :param x: First number
        :param y: Second number
        :return: Difference of x and y
        """
        return x - y

    @staticmethod
    def multiply(x, y):
        """
        Multiply two numbers.

        :param x: First number
        :param y: Second number
        :return: Product of x and y
        """
        return x * y

    @staticmethod
    def divide(x, y):
        """
        Divide two numbers.

        :param x: First number
        :param y: Second number
        :raises ValueError: If y is zero
        :return: Quotient of x and y
        """
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y
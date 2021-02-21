class FizzBuzz:
    def getNumbersUpTo(self, max_number):
        result = ""
        for i in range(1, max_number + 1):
            result += self.getValue(i) + "\n"

        return result

    def getValue(self, number):
        if number % 15 == 0:
            return "FizzBuzz"

        if number % 3 == 0:
            return "Fizz"

        if number % 5 == 0:
            return "Buzz"

        return str(number)

if __name__ == '__main__':
    fizzBuzz = FizzBuzz()
    result = fizzBuzz.getNumbersUpTo(100)
    print(result)
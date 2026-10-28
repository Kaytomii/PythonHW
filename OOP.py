class MyIntArray:
    def __init__(self, numbers=list()):
        self.__numbers = numbers.copy()

    def __str__(self):
        return f"Numbers: {self.__numbers}"

    def __add__(self, other):
        if isinstance(other, MyIntArray):
            if len(self.__numbers) == len(other.__numbers):
                return MyIntArray(self.__numbers + other.__numbers)
            else:
                print("Size of array dont equal")
                return None

arr_1 = MyIntArray([10, 20, 40])
arr_2 = MyIntArray([20, 40, 50])

print(arr_1 + arr_2)
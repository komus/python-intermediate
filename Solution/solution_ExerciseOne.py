### Question One

class Calculator:
    def __init__(self):
        self.__memory = 0

    def add(self, number):
        self.__memory += number # self.__memory = self.__memory + number
        return self.__memory

    def sub(self, number):
        self.__memory -= number
        return self.__memory

    def multi(self, number):
        self.__memory *= number
        return  self.__memory

    def div(self, number):
        self.__memory /= number
        return self.__memory

    def sqroot(self):
        self.__memory = sqrt(self.__memory)
        return self.__memory

    def reset(self):
        self.__memory = 0

    @property
    def memory(self):
        return self.__memory


### Question Two
s1 = "Hello"
s2 = "vufigsaHudesdflelio"

def extract_string(string1:str, string2:str) -> str:
    c_string1 = Counter(string1)
    c_string2 = Counter(string2)

    intersect = c_string1 & c_string2
    
    if intersect == c_string1:
        return f"Possible to make {string1} from {string2}"
    else:
        return f"Not Possible to make {string1} from {string2}"

extract_string(s1, s2)

## OR
count = 0
for ch in s1.lower():
    if ch in s2.lower():
        count += 1

if count == len(s1):
    print("Possible")
else:
    print("Not possible")


### Question 3
list1 = [2,3,4,5,2,3,4,7,-9999,9,3,4]
def sum_number(nums:List) -> float:
    sum = 0
    for x in nums:
        if x != -9999:
            sum += x
        else:
            break
    return sum

sum_number(list1)
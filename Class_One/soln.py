from collections import Counter
# Solution to Exercise

# Question One


# Question 2
s1 = "Hellok"
s2 = "vufigsaHudesdflelio"

#soln
def string_creation(s1, s2):
    counter = 0
    for ch in s1.lower():
        if ch in s2.lower():
            counter += 1 # counter = counter + 1

    if counter == len(s1):
        return True
    else:
        return False

string_creation(s1, s2)

#OR
# Use a class called Counter

print(Counter(s2))

# Question 3
#postional argument
nums = [1, 2,3,4,5,4,2,-9999, 8.9, 7,9,10]

def sum_num_list(nums:list):
    sum = 0
    for x in nums:
        if x != -9999:
            sum += x # sum = sum + x
        else:
            break
    return sum

print(sum_num_list(nums))
        

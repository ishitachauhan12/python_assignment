import pickle
import csv


# 3. Create a script in python and read from the console to create a list of dict for a list of hospitals.
# eg : [{‘hospital_name’:’yashoda’, ‘address’ : ‘test’}]
def input_hopital_data():
    inputData = dict()
    ans = list()

    while True:
        data = input("Input hospital data?(y/n):\n")
        if data == "n":
            break
        else:
            name = input("Input hospital name:\n")
            address = input("Input hospital address:\n")

            inputData["hospital_name"] = name
            inputData["address"] = address
            ans.append(inputData)
    return ans


def pickle_data():
    ans = input_hopital_data()
    with open("Q3.pkl", "wb") as f:
        pickle.dump(ans, f)


def read_pickle_data():
    with open("Q3.pkl", "rb") as file:
        hospitals = pickle.load(file)
        print(hospitals)
    return hospitals


def write_pickle_data_in_csv():
    hospitals = read_pickle_data()
    with open("Q3.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(hospitals)


# pickle_data()
# read_pickle_data()
# write_pickle_data_in_csv()

# 4. Write a function that takes in a non empty array of distinct integers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
# If no two numbers sum up to target sum, the function should return an empty array.
# Note that the target sum has to be obtained by summing two diff integers in the array; you can’t add a single integer to
# itself in order to obtain the target sum.
# You can assume that there will be at most one pair of numbers summing up to the target sum.
# Array = [3, 5, -4, 8, 11, 1, -1, 6]
# Targetsum = 10
# Sample output
# [-1,11]

a = [3, 5, -4, 8, 11, 1, -1, 6]


def two_sum(arrayList, target):
    ans = list(list())
    n = len(arrayList)
    for x in range(len(arrayList)):
        if target - arrayList[x] in arrayList[x:n]:
            ans.append((arrayList[x], target - arrayList[x]))
    print(ans)


# two_sum(a, 10)


# 5. Find all of the numbers from 1–1000 that are divisible by 8 using list comprehension.


def divisible_by_8():
    ans = [x for x in range(8, 1000) if x % 8 == 0]
    print(ans)


# divisible_by_8()

# 6. Count the number of spaces in a string using list comprehension. Eg string : “my name is Khan”.


def countSpaces(string):
    ans = [x for x in string if x == " "]
    print(len(ans))


# countSpaces("my name is Khan")


# 7. Remove all the vowels from a string using list comprehension.


def vowels(string):
    ans = [x for x in string if x.lower() not in "aeiou"]
    print(ans)


# vowels("mynameisKhan")


# 8. “A Python list comprehension consists of brackets containing the expression, which is executed
# for each element along with the for loop to iterate over each element in the”
# Find all the words in the string having length less than 4 letters using list comprehension.


def words_less_than_4(string):
    arr = string.split()
    ans = [x for x in arr if len(x) < 4]
    print(ans)


# words_less_than_4("my name is Khan")


# 9. words = ['data', 'science', 'machine', 'learning']
# Using dict comprehension create a dict having list items and their length as value.
# Example : {‘data’ : 4}


def words_with_length(array):
    ans = {x: len(x) for x in array}
    print(ans)


# words_with_length(["data", "science", "machine", "learning"])


# 10. Write a function that takes in a non empty array of integers that are sorted
# in ascending order and returns a new array of same length with the square of original
# integers also sorted in ascending order.
# Sample input : [1,3,5,6]
# Sample output : [1,4,925, 36]


def sorted_square(array):
    ans = list()
    for i in array:
        ans.append(i**2)
    print(ans)


# sorted_square(a)


# 11. You are given a list of integers and an integer. Write a function that moves all
# instances of that integer in the list to the end of the list and returns the list.
# Sample input : [2,1,2,2,2,3,4,5]
# toMove = 2

# Sample output : [1,3,4,2,2,2,2,2]

b = [2, 1, 2, 2, 2, 3, 4, 2, 5]


def move_target_at_last(array, target):
    st = 0
    en = len(array) - 1
    while st < en:
        if array[st] == target:
            array[st], array[en] = array[en], array[st]
            en -= 1
        else:
            st += 1
    print(array)


move_target_at_last(b, 2)

# errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

# print(enumerate(errands))

# for idx, task in enumerate(errands, 1):
#     print(f"{task} is number {idx} on my list of things to do today!")


# def iterate_list(numbers):
#     total = 0
#     for number in numbers:
#         if number % 2 == 1:
#             total+= number

    
#     return total
# total = iterate_list([1,2,3,4,5])
# print(total)

# def sum_of_odd(numbers):
#     total = 0
#     for number in numbers:
#         if number % 2 == 0:
#             total = total + number
#     return total
# total = sum_of_odd([1,2,3,4,5])
# print(total)

# d

# def product_of_even(numbers):
#     total = 1
#     for number in numbers:
#         if number % 2 == 0:
#             total *= number
#     return total
# total = product_of_even([1,2,3,4,5])
# print(total)



def concatenated(strings):
    result = ""
    for string in strings:
        if len(string)>2:

            result += string
    return result
print(concatenated(["abc", "def", "ghi"]))










# def greatest_number(numbers):
#     greatest = numbers[0]
#     for number in numbers:
#         if number > greatest:
#             greatest = number
#     return greatest
# print(greatest_number([1,5,6,7]))

# def concatenate(strings):
#     character = ""
#     for string in strings:
#         if len(string) > 2:
#             character += string
#     return character
# print(concatenate(["abc", "def", "ghi"]))
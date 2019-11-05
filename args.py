def sum_of_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_of_numbers(1,5,5,8,5,8,2,5,))
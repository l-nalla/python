def sum_of_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
print(sum_of_odd_numbers([1,2,3,4,5,6,7,8,9]))


#It will return value after excuting the if loop it doesn't check whole for loop
#return statement will exists after excuting the return statement
#def sum_of_odd_numbers(numbers):
#    total = 0
#    for num in numbers:
#        if num % 2 != 0:
#            total += num
#        return total
#print(sum_of_odd_numbers([1,2,3,4,5,6,7,8,9]))

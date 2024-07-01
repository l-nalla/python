nested_list = [[1,2,3],[4,3,2],[3,5,6]]
print(nested_list)

print(nested_list[-1][1])

print(nested_list[1][2])

#for l in nested_list:   #for printing all values in the lists
 #   for val in l:
  #      print(val)


[[print(val) for val in l]for l in nested_list]


board = [[num for num in range(1,5)]for val in range(1,4)]
print(board)

a = set('abcdefghijklmnopqrstuvwxyz')
b = set('laxmareddy')

print(a|b)

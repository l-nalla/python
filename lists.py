first = [1,2,3,4,5,6,7,8,9,10]
print(first)  #prints the data in list

first.append(21)
print(first)  #adds a single value to list at end

first.append(int(input("enter the desired value")))
print(first)
first.extend([22,2,10,10])
print(first)  #adds multiple values to list at end

first.insert(2,'hii')   
print(first)    #adds the value at desired position

first.remove(21)
print(first)    #removes the given element

first.remove('hii')

first.pop(1)
print(first)    #removes the value at given indexed position



first.count(10)

first.reverse()
print(first)    #reverses the list

print(first[3:])    #prints from the given index value

print(first[:3])    #prints upto given index value

print(first[2:10])  #prints the values b/w given indices

del first[0]
print(first)    #deletes the value in the given index value

del first[2:4]
print(first)   #delete the values in b/w given indices values




#List Comprehensions
#squares = []
#for i in range(10):
    #squares.append(i**2)
    #print(squares)

squares = [x**2 for x in first]
print(squares)

#list = [(x,y)for x in first for y in first.reverse() if x!=y]
#print(list)

print("\U000f1600")

first.sort()
print(first)    #sorts the string in a proper order

first.clear()
print(first)    #clears all items in the list



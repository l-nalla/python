#Dictionaries will use the key and value pair to represent value in the dictionary
#key:value 
#Here the key is a string and value is a integer
telugu = {'dot':121,'comma':142,'beta':423}
print(telugu['dot'])    #prints the value of the given key

#we can delete a key:value pair by giving the key to delete the whole pair
del telugu['comma'] #this will delete the pair of 'comma'
print(telugu)


print(list(telugu)) #prints the key values as a list

print(sorted(telugu))   #prints the key values in a sorted manner

print('dot' in telugu)  #checks whether the key is in dictionary or not in boolean way

print('jack' in telugu) 

print(telugu.keys())    #it will print the keys contained in a dictionary

print(telugu.values())  #it will print the values containedc in a dictionary

print(telugu.items())   #it will print the items along with key:value in dictionary

for k,v in telugu.items():
    print(f"key is {k} and value is {v}")

ntelugu = {}.fromkeys('a','b')
print(ntelugu)

ntelugu = {}.fromkeys('sfhs',12412)
print(ntelugu)
ntelugu = {}.fromkeys('e','r')
print(ntelugu)
print(ntelugu.get('hello'))
#dict([('sape',1342),('lamda',1433),('neon',1434)])
#print(telugu)


#Eaxmple of tuple's

t = 123,232,424,533
print(t[0])     #prints the given index value
print(t)        #prints the all values in the given
print(t.index(123))
#tuple's can be nested in another tuple

u = t, (144,546,754,764)
print(u)        #prints values in t and u by seperating the tuple's with braces and a comma

#t[0] = 341
#print(t)   tuple's are immutable they can't be replaced


v = ([1,2,3],[3,2,1])
print(v)    #lists can be assigned to a tuple


months = ('January','February','March','April','May','June','July','Augest','September','October','November','December')
for month in months:
    print(month)

i = len(months) - 1
while i >= 0:
    print(  months[i])
    i -= 1

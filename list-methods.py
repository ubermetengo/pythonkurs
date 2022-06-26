from traceback import print_last


numbers = [ 1, 2, 3, 4, 5, 6, 3]
letters = [ "a" , "g","f", "x" , "y", "a", "s"] 

print(min(numbers))
print(min(letters))
print(max(numbers))
print(max(letters))

print(numbers[3:6])
print(numbers[::-1])
numbers.append(31)
print(numbers)

numbers.insert(4,22)
print(numbers)

listC = [112,132,11,41]
listC.remove(112)
print(listC)
listC.sort()
print(listC)
print(listC.count(132))

#Using the next list do:

#29, 18, 6 25, 5, 15, 19, 3, 45, 2
#1. Get the numbers who are divisor of other number in the list.
#2. Count how many dividend has a divisor.
#3. Sort the list putting first even and then odd numbers.

#Gabriel Barrantes Jara

num_List = [29, 18 ,6 ,25, 5, 15, 19, 3, 45, 2]

def getDivisorsOnList():
	divisors = list()
	for x in num_List:
		for y in num_List:
			if(x != y and y%x == 0):
				if(x not in divisors):
					divisors.append(x)
	return divisors

			

	
def getCountDivisors():	
	for x in num_List:
		counter = 0
		for y in num_List:
			if(x!=y and x%y == 0):
				counter+=1
		print(str(x)+" has "+str(counter)+" divisors.")





def sortListByEven():
	temp_val = 0
	
	for x in range (len(num_List)):
		for y in range (len(num_List)):
			if(x!=y):
				if(num_List[x]%2 == 0 and num_List[y]%2 != 0):
					temp_val = num_List[x]
					num_List[x] = num_List[y]
					num_List[y] = temp_val


	return num_List
    

print("Divisors: "+str(getDivisorsOnList()))
getCountDivisors()
print("Sorted List By Even Numbers: "+str(sortListByEven()))





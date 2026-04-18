#sequential searching algorithm (assigned member: Gerald D. Boniel)


"""
SO i will implement just a straight one-way search from start to finish 
unlike binary search (with the ordered elements) that halves the array, which is a faster algo that I am familiar wth.
So array [0 - nth index] 
will just iterate each index if it's the element we are searching for and if true then we can return that index. 

as for testing this I will use random.choice(data)  # which will produce a random number from the random int list
"""


import random 


def sequential_searching(data: list, element:int) -> int | None:   #index is int and None if the element is not on the list 
	for i in range(len(data)):
		if data[i] == element:
			return i
	return None


def main():
    N = 100000  #I opted to use medium data set
    data = [random.randint(1, 1000000) for _ in range(N)]
    
    element = random.choice(data)  #element I will be using that is on the data
    non_element = -67   #not an element of the list (I just used negative since this is obviosuly not part of the range in data)
    

    
    
    
    #Search an existing elment in the array
    print(f"Number we are looking for is: {element}.")
    index1 = sequential_searching(data, element)
    print(f"The number {element} is at index {index1},")
    
    
    #Search a non element in the array
    print(f"\nNumber we are looking for is: {non_element}.")
    index2 = sequential_searching(data,non_element)
    
    if index2 is None:
        print(f"The number {non_element} is not on the list.")
    

if __name__ == "__main__":
    main()

# Keenan Kimbrough November 18, 2022


def bubblesort(list_a):
    indexing_length = len(list_a) - 1 # "-1" because you can not do a swap on the last element
    sorted = False
    while not sorted:
        sorted = True # once the elements have all been sorted, this will active and will break the loop
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #swaping
    return list_a
list_a = [19,2,31,45,6,11,121,27]

print(bubblesort(list_a))


"""
    Understanding:
    Bubble sort takes in an unsorted list and then compares the first 2 elements in the array
    and then swaps the numbers if the higher number is on the right side. then it keeps comparing the next elements contiunously until the highest number is at the top.
    That ends the first iteration. Then it starts over and continues until the second highest number is next to last.
    These iterations continues until the entire list is sorted, then the loop breaks and an sorted list is given back.
    
    Time Complexity of Bubble Sort
    Worse Case Time Complexity of O(N)^2
    Space Complexity of O(1)
    
    Notes - The number of swaps in bubble sort equals the number of inversion pairs in the given array.
    when the array elements are few and the arrray is nearly sorted, bubble sort is effective and efficent
    
    
    Summary: compares adjavcent elements and swaps them if they are out of order.
    Hint: elements bubble at the top of the list
    
    Future: I need to figure out how to manipulate and transform if needed for better optimzation
    
 """
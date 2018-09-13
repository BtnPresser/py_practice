# The purpose of this excercise is to reverse a given list

exList = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e','f','g']

# The idea here is to simply return the list that we had but step through it backward before doing so.
# This however will create a new list, what if we want to return it without creating a new one?
def reverse_list(p_list):
    return p_list[::-1]

# To make this work we need to keep track of indexes and step through the list ourselves
# whilst flipping elements with each other
def reverse_list_in_place(p_list):

    # indexes
    left = 0
    right = len(p_list) -1

    # When we pass the midpoint we have finished
    while left < right:
        # swap elements
        temp = p_list[left]
        p_list[left] = p_list[right]
        p_list[right] = temp

        # update indexes
        left += 1
        right -= 1

    return p_list

#if __name__ == "__main__":
print("This is the result of a new reversed list being returned:\n\t" + str(reverse_list(exList)) + "\n")
print("This is the result of the same list being returned with inplace swapping:\n\t" + str(reverse_list_in_place(exList)))
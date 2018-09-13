# The purpse of this script is to determine the sum of a list with different looping methods

def for_loop_sum(plist):
    sum = 0
    for num in plist:
        sum += num

    return sum


def while_loop_sum(plist):
    sum = 0
    index = 0
    while index < len(plist):
        sum += plist[index]
        index += 1

    return sum


def recursive_sum(p_list, pindex):
    if pindex < len(p_list):
        return p_list[pindex] + recursive_sum(p_list,pindex+1)
        
    # End case    
    return 0

exList = [1,2,3,4,5,6,7,8,9,10]

if __name__ == "__main__":
    print("For loop sum of a list: " + str(for_loop_sum(exList)))
    print("While loop sum of a list: " + str(while_loop_sum(exList)))
    print("Recursive sum of a list: " + str(recursive_sum(exList, 0)))
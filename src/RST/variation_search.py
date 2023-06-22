from rst import RST
import numpy as np
import matplotlib.pyplot as plt


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]

if __name__ == "__main__":
    print("Variation in search complexity")
    tree = RST()

    """
    1. Insert a number of keys
    2. Do a large number of searches and keep track of complexity
    """

    N = range(1000, 131000, 1) # range(500, 130000, 500)
    X = []
    Y = []
    
    print("Inserting elements...")
    # insert 2000 elements
    for n in N:
        tree.insert(n)
    
    # print("Inserted ", len(N), " elements.")
        
    # average of NUM_SEARCHES searches
    NUM_SEARCHES = 4000
    dicto = {}

    for s in range(NUM_SEARCHES):
        (s_res, depth) = tree.search(s)
        # add one to the value with key depth
        #print("search depth ", depth)
        if depth not in dicto:
            # insert new key
           # print("insert new key: ", depth)
            dicto[depth] = 1
        else:
            # update exiting key
            # print("update new key: ", depth)
            current_val = dicto[depth]
            # print("current_val: ", current_val)
            dicto.update({depth : (current_val+1)})
    
    for key in sorted(dicto):
        (key, dicto[key])
        # print(key, dicto[key])
        X.append(key)
        Y.append((dicto[key]/NUM_SEARCHES)*100) # calculate percentages

    # print("X :", X)
    # print("Y :", Y)

    plt.plot(X, Y)
    plt.xlabel('Complexity i')
    plt.ylabel('Percentage of searches with complexity i')
    plt.title("130.000 Elements - 4000 Searches")
    plt.show()
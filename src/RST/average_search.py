from rst import RST
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Average Search Complexity")
    tree = RST()

    N = range(500, 130000, 500) #[5000, 10000, 20000, 40000, 80000, 100000, 110000, 120000, 130000]
    Y = []

    # insert 2000 elements
    for n in N:
        # insert the number og elements
        for e in range(n):
            tree.insert(e)
        
        # average of NUM_SEARCHES searches
        NUM_SEARCHES = 3000
        complexity_sum = 0
        for s in range(NUM_SEARCHES):
            (s_res, depth) = tree.search(s)
            complexity_sum += depth

        Y.append(complexity_sum/NUM_SEARCHES)    


    plt.plot(N, Y)
    plt.xlabel('Number of Elements')
    plt.ylabel('Complexity - Average Depth of node')
    plt.show()




        
    
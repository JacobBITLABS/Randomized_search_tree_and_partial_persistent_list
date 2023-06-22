from ll import LL
import random
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("[Space vs. Pointer Test]")
    LList = LL()
 
    X = range(1, 100, 2) # allowed modifications 1,3,...
    Y = [] # space 

    for x in X:
        NUM_ELEMS = 1000
        N = list(range(0, NUM_ELEMS, 1))

        for _ in range(0, NUM_ELEMS):
            i  = random.randint(0, len(N))
            selection = random.randint(0, len(N)-1)
            i_key = N.pop(selection)

            # make k_mark?
            k_mark = random.uniform(0, 1)

            # if not below 0.33, do not insert.
            if k_mark > 0.33:
                k_mark = None
            else:
                k_mark= i_key+1

            LList.insert(index=i_key, key=i_key+1, k_mark=k_mark)

        Y.append(LList.n_space_alloc)

    


    plt.plot(X, Y)
    plt.xlabel('Number of Extra Pointers')
    plt.ylabel('Number of Allocations')
    plt.show()
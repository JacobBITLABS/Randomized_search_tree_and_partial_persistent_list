import sys
from LinkedList.ll import LL
from RST.rst import RST

def main(argv):
    if len(sys.argv) > 4:
        print("Please only call me with one parameter")
        sys.exit()

    if sys.argv[1] == "PLL":
        print("Persistent Linked List")

        PLL = LL() 
        inputFile = sys.argv[2]

        print(inputFile)
        with open(inputFile, "r") as txt:
            for line in txt:
                for line in txt:
                    operation = line[0]
                    print(operation)
                    index = line[2]
                    key = line[4]
                    k_mark = line[6] # -1 or val
                    # do operation
                    if operation == "I":
                        # print("Insert")
                        if k_mark == -1:
                            k_mark = None
                        v = PLL.insert(index=int(index), key=int(key), k_mark=k_mark)
                    elif operation == "U":
                        PLL.update(int(index), int(key))

                    elif operation == "S":
                        print("Search")
                        version = int(index)
                        _key = int(key)
                        (n0_key, n0_data) = PLL.search(version=version, index=_key)
                        print("n0.key: ", n0_key, " n0_data", n0_data.key())

                        output = operation + " key: " + str(n0_key) + "  |  " + "data " + str(n0_data.key()) + "\n"
                        sys.stdout.write(output)
                        sys.stdout.flush()

                    else:
                        print("Only accepted operations arguments are I and S")
                        sys.exit()
        
    elif sys.argv[1] == "RST":
        # p = sys.argv[2]
        print("Randomized Search Tree")
        
        # construct Skip List
        rst = RST()
        inputFile = sys.argv[2]
        
        with open(inputFile, "r") as txt:
            for line in txt:
                operation = line[0]
                val = line[2] 
                # do operation
                if operation == "I":
                    rst.insert(int(val)) # val = key
                    output = operation + ": Inserted " + val + "\n"
                    sys.stdout.write(output)
                    sys.stdout.flush()

                elif operation == "S":
                    (s_res, depth) = rst.search(int(val))
                    output = operation + " " + str(s_res) + "in depth " + depth + "\n"
                    sys.stdout.write(output)
                    sys.stdout.flush()

                elif operation == "D":
                    output = operation + ": Look in rst.py line 248\n"
                    sys.stdout.write(output)
                    sys.stdout.flush()

                else:
                    print("Only accepted operations arguments are I, D and S")
                    sys.exit()

    else:
        print("Only accepted arguments are f, i and w")
        sys.exit()



if __name__ == "__main__":
   main(sys.argv[1:])
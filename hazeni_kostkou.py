import sys
import random
    
print([random.randint(1, int(sys.argv[1])) for i in range(int(sys.argv[2]))])


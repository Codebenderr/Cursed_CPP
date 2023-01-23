import os
import sys
import cursed_cpp

argCount = len(sys.argv)
if argCount == 3:
    with open(sys.argv[1], 'r') as f:
        with open('uncursed_' + sys.argv[1], 'w') as f2:
            f2.write(cursed_cpp.uncurse(f.read()))
            compiler = sys.argv[2]
            os.system(f"{compiler} {sys.argv[1]}")
            
            
elif argCount == 4:
    with open(sys.argv[1], 'r') as f:
        with open(sys.argv[2], 'w') as f2:
            f2.write(cursed_cpp.uncurse(f.read()))
            compiler = sys.argv[3]
            os.system(f"{compiler} {sys.argv[2]}")
    


import os

print("pid before forking")
print(os.getpid())

newpid = os.fork()
if newpid == 0:
    print("forking succesfull")
    print("making some system calls!!!")
    print(os.uname())
    print("Done")
print(newpid)

newpid2 = os.fork()
print("making second child")
if newpid2 == 0:
    print("forking succesfull")
    print(newpid2)
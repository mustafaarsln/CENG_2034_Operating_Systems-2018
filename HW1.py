import os

print("pid before forking")
print(os.getpid())

firstpid = os.fork()
if firstpid == 0:
    print("forking succesfull")
    print("making some system calls!!!")
    print(os.uname())
    print("Done")
print(firstpid)

secondpid = os.fork()
print("making second child")
if secondpid == 0:
    print("forking succesfull")
    print(secondpid)

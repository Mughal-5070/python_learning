#   *
#  ***
# *****

num = int(input('Enter a number: '))

for i in range (num+1):
    print (" "*(num-i),end="")
    print ("*"*(i*2-1),end="")
    print ("")
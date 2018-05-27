
"""fizzcheck"""
def fizzcheck(x):
    truecheck = False
    if(x % fizz == 0):
        return(truecheck == True)
    else:
        return(truecheck)
"""buzzcheck"""
def buzzcheck(x):
    truecheck = False
    if(x % buzz == 0):
        return(truecheck==True)
    else:
        return(truecheck==False)
"""mainline"""""
fizz = input("Please enter the number for fizz: ")
buzz = input("Please enter the number for buzz: ")
fizzbuzz = fizz*buzz
for count in range(0,100):
    boolfizz = fizzcheck(count)
    boolbuzz = buzzcheck(count)
    if(boolfizz == True & boolfizz==boolbuzz):
        print("FizzBuzz!")
    elif(boolfizz == True & boolfizz!=boolbuzz):
        print("Fizz!")
    elif((boolfizz != True & boolfizz!=boolbuzz)):
        print("Buzz!")
    else:
        print(count)
end


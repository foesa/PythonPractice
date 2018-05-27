
"""fizzcheck"""
def fizzcheck(x):
    truecheck = False
    if x % fizz == 0 and x != 1:
        truecheck = True
        return truecheck
    else:
        return truecheck

"""buzzcheck"""
def buzzcheck(x):
    truecheck2 = False
    if x % buzz == 0 and x != 1:
        truecheck2 = True
        return truecheck2
    else:
        return truecheck2

"""mainline"""""
fizz = int(input("Please enter the number for fizz: "))
buzz = int(input("Please enter the number for buzz: "))
fizzbuzz = fizz*buzz
for count in range(1,100):
    boolfizz = fizzcheck(count)
    boolbuzz = buzzcheck(count)
    if boolfizz == True and boolfizz == boolbuzz :
        print("FizzBuzz!")
    elif boolfizz == True and boolfizz != boolbuzz:
        print("Fizz!")
    elif boolfizz == False and boolfizz != boolbuzz:
        print("Buzz!")
    else:
        print(count)
end


finished = False
number = 0
oldAverage = 0
oldVariance = 0
while (not finished):
    number = number +1
    enteredInput = input("Please enter a number or type 'Exit': ")
    if (enteredInput == "exit"):
        finished = True
    else:
        numberEntered = int(enteredInput)
        average = oldAverage + (numberEntered - oldAverage)/number
        variance = ((oldVariance * (number - 1)) + (numberEntered - oldAverage) * (numberEntered - average)) / number
        print("So far the average is", average, "and the Variance is ", variance)
        oldVariance = variance
        oldAverage = average



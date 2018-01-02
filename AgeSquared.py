import math
currentYear = 2018
maxAge = 123
age = 45
ageSquared = age*age
if ageSquared>currentYear-maxAge and ageSquared<currentYear+maxAge:
    birthYear = (ageSquared - age)
    if birthYear<(currentYear + maxAge) and birthYear >(currentYear - maxAge) and birthYear <= currentYear:
        print("In the year", ageSquared, "you would be", age)






def person(probability:float) -> int:
    n = 1
    p = 1
    while p > (100-probability)/100:
        p *= ((365 - n)/365)
        n+=1
    if n > 365:
        n = 365
    return n
def probability(persons:int) -> float:
    if persons > 152:
        return 1
    p = 1
    for i in range(0, persons):
        p *= ((365-i)/365)
    return 1-p
print("""This is a calculator for the birthday problem
------------------------------------------------------------------------------------------------------------------------
Insert 1 to calculate the probability of get two or more persons that has the same birthday with n persons
Insert 2 to calculate the number of persons needed to get the probability n of have two or more persons with the same birthday""")
op = 0
while op == 0:
    try:
        op = int(input('Insert an option: '))
        if op == 1:
            n = int(input('Insert the number of persons: '))
            if n < 1:
                n = 1
                raise AttributeError('The number of persons must be one or more. Setting to 1')
        elif op == 2:
            n = float(input('Insert the probability: '))
            if n < 0:
                n = 0
                raise AttributeError('The probability must be equal or more than 0%. Setting to 0%')
            elif n > 100:
                n = 100
                raise AttributeError('The probability must be equal or menor than 100%. Setting to 100%')
        else:
            op = 0
            raise AttributeError('Insert 1 or 2')
    except ValueError:
        print('Please insert a number')
        op = 0
    except AttributeError as error:
        print(error)
if op == 1:
    print("The probability is " + str(probability(persons=n)*100) + "%")
else:
    print("You need " + str(person(probability=n)) + " persons")
input('Press any key to exit... ')
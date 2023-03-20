''' ***Basic Calculator*** '''
'''operators (+),(-),(*),(/),(%),(sqrt)'''
import math
print()
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y
def percentage(x, y):
  return (x * y) / 100.0
print("Select Operation among these.")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Percentage")
print("6.Square root")

while True:
    choseOperator = input("Enter the operator you want: ")
    if choseOperator in ('1', '2', '3', '4', '5'):
        try:
            numb1 = int(input("Enter first number: "))
            numb2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input.Please enter a number.")
            continue
        if choseOperator == '1':
            print(numb1, '+', numb2, '=', add(numb1, numb2))
        elif choseOperator == '2':
            print(numb1, '-', numb2, '=', sub(numb1,numb2))
        elif choseOperator == '3':
            print(numb1, '*', numb2, '=', mult(numb1, numb2))
        elif choseOperator == '4':
            print(numb1, '/', numb2, '=', div(numb1, numb2))
        elif choseOperator == '5':
            print(percentage(numb1, numb2), "%")
        nextCalculation = input(" Do you want to do the next calculation(yes/no): ")
        if nextCalculation == 'no':
            break
    elif choseOperator == '6':
        try:
           num = int(input("Enter the number: "))
        except ValueError:
            print("Please try again")
            continue
        if choseOperator == '6':
            print(num,'sqrt is',math.sqrt(num))
        nextCalculation = input(" Do you want to do the next calculation(yes/no): ")
        if nextCalculation == 'no':
            break
    else:
        print("Invalid input.")

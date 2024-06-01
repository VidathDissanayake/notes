#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError: 
        print('float division by zero')
        return None

def power(a, b):
    return a ** b

def remainder(a, b):
    try:
        return a % b
    except ZeroDivisionError: 
        print('float division by zero')
        return None

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def get_input(number):
    n = input(f'Enter {number} number: ')
    print(f'{n}')
    if '$' in n:
        return None
    elif '#' in n:
        print("Done. Terminating")
        exit()
    else:
        n = float(n)
        return n
        

def select_op(choice):
    if choice == '#':
        return -1
    check = True
    a = get_input('first')
    if a == None:
        check = False
    else:
        b = get_input('second')
        if b == None:
            check = False

    if choice != '$' and check:
        try:
            if choice in ['+','-','*','/','^','%']:
                if choice == '+':
                    o = add(a, b)
                elif choice == '-':
                    o = subtract(a, b)
                elif choice == '*':
                    o = multiply(a, b)
                elif choice == '/':
                    o = divide(a, b)
                elif choice == '^':
                    o = power(a, b)
                elif choice == '%':
                    o = remainder(a, b)
                print(f'{a} {choice} {b} = {o}')
            else:
                print("Unrecognized operation")
                return None
        except ValueError:
            print("Not a valid number, please enter again")
            return None



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()
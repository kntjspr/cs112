import os
os.system("title Laboratory Activity 2.3: Python Functions (Implementation)")

def basic_function(num1, num2) -> int:
    return int(num1) + int(num2) 

def string_manipulation(string) -> str:
    return string[::-1] # Reverses string using slice

def list_processing(l):
    l = l.replace(' ', '') # Remove possible spaces before comma
    l = l.split(",") 
    result = []
    for i in l:
        try:
            if int(i) % 2 == 0:
                result.append(i)
        except: # Ignores non-integer in current iteration
            continue
    return result

def conditional_logic(num) -> str:
    try:
        if int(num) % 2 == 1: # Determining odd/even by using modulo/remainder
            return 'Odd'
        else:
            return 'Even'
    except:
        print('An error has occured. Make sure that your input is a digit.')

def personal_info(name, age, occupation='N/A'):
    return f"\n\nName: {name}\nAge: {age}\nOccupation: {occupation}"

def collatz(num):
    result = []
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (3 * num) + 1
        result.append(num)
    return result

def integrated(num):
    """
    Algorithm:
        1. Call the collatz function. The collatz function must have a return statement (i.e, list).
        2. Iterate over the returned value from calling the collatz function;
        3. For each iteration, you must apply the linear function with the given values for m and b;
            m = 0.5
            b = 1
        4. Return all results from calling the linear function in a list.

    Example Output:
        linear_sequence = integrated(20)
        >>> [6.0, 3.5, 9.0, 5.0, 3.0, 2.0, 1.5]
    """
    result = [] # Initialize empty list
    value = collatz(num) # Set the result of collatz function to a variable named value
    linear = lambda x, m=0.5, b=1: (m*x) + b # Create linear lambda
    for i in value: # For each iteration of collatz list
        result.append(linear(i)) # Append to result list
    return result # Returns result


def menu():
    print(f"{GREEN}Laboratory Activity 2.3: Python Functions (Implementation)\n\n{RESET}1. Arithmetic (Basic Function)\n2. String Manipulation\n3. List Processing\n4. Conditional Logic\n5. Default Parameters\n6. Integrating Collatz and Linear function")
    i = input("\nSelect a choice (1-6): ")
    try:
        match i:
            case '1':
                print('\n\nBasic arithmetic calculator')
                print('Function: You will give me two integers then I will return the sum of two numbers.\n')
                num1 = input("Enter first number: ")
                print(f"{num1} + ?")
                num2 = input("Enter second number: ")
                print(f"{GREEN}Result: {basic_function(num1, num2)}{RESET}")
            case '2':
                print('\n\nString manipulation: String reverser')
                print('Function: You will input a string and then I will return it in reversed order.\n')
                s = input("Enter a string to be reversed: ")
                print(f"{GREEN}Reversed string: {string_manipulation(s)}{RESET}")
            case '3':
                print('\n\nList processing: Even numbers parser.')
                print('Give me a list of numbers and I return the even numbers only.')
                l = input("Enter numbers (separated by comma): ")
                print(f"{GREEN}Even numbers: {list_processing(l)}{RESET}")
            case '4':
                print("\n\nConditional logic: Odd/Even identifier")
                print("Give me a number and I will determine if the number is odd or even.")
                num = input("Enter a number: ")
                print(f"{GREEN}The number is: {conditional_logic(num)}{RESET}")
            case '5':
                print("\n\nDefault parameters: Personal Info")
                print("Prints your personal info but with optional values via default parameters.")
                name = input("Enter your name: ")
                age = input("Enter your age: ")
                occupation = input("Enter your occupation (Leave blank if not applicable): ")
                if not occupation: # Checks if occupation input is a blank string.
                    print(f"{GREEN}{personal_info(name,age)}{RESET}")
                else:
                    print(f"{GREEN}{personal_info(name,age,occupation)}{RESET}")
            case '6':
                print("Integrating Collatz and Linear Function")
                linear_sequence = input("Enter an integer: ")
                try:
                    print(f"{GREEN}Linear sequence: {integrated(int(linear_sequence))}{RESET}")
                except ValueError:
                    print(f"{RED}Non int values are not accepted.{RESET}")
            case _: # Default case
                print(f"{RED}Put a valid option from 1 - 6. Try again. {RESET}")
                input("Press enter to continue. ")
                os.system('cls')
                menu()
    except ValueError:
        print(f"{RED}Put a valid number. Try again.{RESET}")
        os.system('cls')
        menu()
    except Exception as err:
        print(f"{RED}An error has occured. Please check the exception\n\n{err}{RESET}")

if __name__ == '__main__':
    # Text color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    menu()
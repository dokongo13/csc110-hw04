# ------------------------------------------------------
#        Name: (Diane Okong'o)
#       Peers: (Esther He, Alice)
#  References: (slides, lecturers)
# We looked at this and we couldn't figure it out why the first 2 tests were failing:(
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    #Allowing user to input secret word
    while True:
        n = input("Enter secret word: ")
        if secret_word in n:
            print("You used the secret word!")
            # I was informed during office hours .lower makes it case sensitive
        #return takes as back to the function def check_text() this is done because the if the function is true and passes the test. If its false it passes onto the next elif statemen as they are mutually exclusive. 
            return
        elif "dog" in n:
            print("\'You used the word \"dog\" or the word \"Dog\"!")
        #Use of backward slash includes the "'" in text it must be placed in front of the quotation mark to be included
            return
        else:
            print("Try again")
        # we do not put return here that would take as out the loop and return the control to function and main

# Task 2
def check_greater():
    #Allow user to input for integers
    while True:
        n = int(input("Enter first integer: "))
        m = int(input("Enter second integer: "))
        if n > m:
            print(f"First is Greater")
            return
        elif m > n:
            print(f"Second is Greater")
            return
        else:
            print("Try again")
        
# Task 3
def get_special_numbers():
    for counter in range(1,41):
        if counter % 2 != 0 and counter % 3 == 0 and counter % 5 != 0:
            print(counter)
        else:
            continue
    
# Task 4.a
def my_for_loop():
    y = input("Give me a string: ")
    if len(y) not in range(2,6) or " " in y:
        print(f"bad word")
        return
    #do i need to make another if statement here
    for let in y:
        if let.lower() in ["a","e","i","o","u"]:
            print(f'letter {let} is a vowel')
        else:
            print(f'letter {let} is a consonant')
              
# Task 4.b
def my_while_loop():
    while True:
        x = input("Choose one option: a, b, or c: ").lower()
        if x == "a":
            continue
        elif x == "b":
            print("Goodbye")
            return
        elif x == "c":
            sys.exit()
        else:
            print("try again")
                
    

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

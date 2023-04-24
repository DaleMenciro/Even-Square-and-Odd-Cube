'''
Write a method in python that will create two separate text files after reading 
the source text file named integers.txt that contains 20 integers. The first output 
file will be named double.txt containing the square of all even integers found in integers.txt
and the second file will be named triple.txt containing the cube of all odd numbers found in the 
integers.txt.
'''
def process_file():
        #read integers from integers.txt
    with open("integers") as input_file:
        integers = list(map(int, input_file.read().split()))
        #extract all even and odd from the list
        even_integers = [n for n in integers if n % 2 == 0]
        odd_integers = [n for n in integers if n % 2 != 0]

        #append square of even numbers to double.txt
        with open("double.txt", "a") as double_file:
            for n in even_integers:
                double_file.write(str(n * n) + "\n")
        
        #append cube of odd numbers to triple.txt
        with open("triple.txt", "a") as triple_file:
            


#====== START =====
    process_file()
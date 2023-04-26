import tkinter as tk
from tkinter import filedialog, messagebox

def process_file():
        #read integers from integers.txt
    with open("integers.txt") as input_file:
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
            for n in odd_integers:
                triple_file.write(str(n * n * n) + "\n")

def browse_input_file_path():
    global input_file_path
    input_file_path = filedialog.askopenfilename()

def browse_output_dir_path():
    global output_dir_path
    output_dir_path = filedialog.askdirectory()

def process_files():
    global input_file_path, output_dir_path
    process_file(input_file_path, output_dir_path)

#====== START =====

input_file_path = ""
output_dir_path = ""

#create main window
#create input file selection button
#create output directory selection button
#create process button

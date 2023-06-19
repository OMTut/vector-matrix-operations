import os
import sys
import time
from mod.vector_operations import *

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.019)
    print()
    
def showTitle(choice):
    os.system('cls||celar')
    if choice == "1":
        typewriter("Vector Addition")
    elif choice == "2":
        typewriter("Vector Subtraction")
    elif choice == "3":
        typewriter("Vector Scalar Multiplication")
    elif choice == "4":
        typewriter("Dot Product")
    elif choice == "5":
        typewriter("Vector Cross Product")
    elif choice == "6":
        typewriter("Vector Length")
    else:
        typewriter("Vector Operations")
    typewriter("===================================================")
    print()

def showMenu():
    typewriter("1. Vector Addition")
    typewriter("2. Vector Subtraction")
    typewriter("3. Vector Scalar Multiplication")
    typewriter("4. Dot Product")
    typewriter("5. Vector Cross Product")
    typewriter("6. Vector Length")
    typewriter("7. Exit")



def createMatrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input("Enter element " + str(i + 1) +
                                  " col " + str(j+1) + ": ")))
        matrix.append(row)
    return matrix

def printVector(vector):
    for i in range(len(vector)):
        print(vector[i], end = ' ')
    print()

def proceed():
    input("Press Enter to continue...")

choice = "0"
while choice != "7":
    showTitle(choice)
    showMenu()
    choice = input("Enter your choice: ")
    if choice == "1":
        showTitle(choice)
        x = createVector()
        y = createVector()
        result = addVectors(x, y)
        print()
        print("Result: ", end='')
        printVector(result)
        print()
        proceed()
        choice = "0"
    elif choice == "2":
        # u = createMatrix()
        # for row in u:
        #     for i in row:
        #         print(i, end=' ')
        #     print()
        showTitle(choice)
        x = createVector()
        y = createVector()
        result = subtractVectors(x, y)
        print()
        print("Result: ", end='')
        printVector(result)
        print()
        proceed()
        choice = "0"
    elif choice == "3":
        showTitle(choice)
        vector = createVector()
        scalar = int(input("Enter a scalar: "))
        result = scalarVectors(vector, scalar)
        print()
        printVector(result)
        print()
        proceed()
        choice = "0"
    elif choice == "4":
        showTitle(choice)
        vector1 = createVector()
        vector2 = createVector()
        result = dotProductVectors(vector1, vector2)
        print()
        print("Result: ", end='')
        print(result)
        print()
        proceed()
        choice = "0"
        


import subprocess
import sys
"""
    A file to run commands that are used in questions on the homework
"""

# subprocess.run([])

n = len(sys.argv)

if n < 2:
    print("Command-line argument needed")

recognized_arguments = ["3a_truthful", "3a_balanced"]

if sys.argv[1] not in recognized_arguments:
    print("Unrecoginzed command-line argument. Try: ")
    print(recognized_arguments)

if sys.argv[1] == "3a_truthful":
    subprocess.run("python3 auction.py --perms 1 --iters 200 --seed 2 Truthful,5".split(" "))
    
elif sys.argv[1] == "3a_balanced":
    subprocess.run("python3 auction.py --perms 1 --iter 200 --seed 2 Basmbb,5".split(" "))

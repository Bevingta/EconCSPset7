import subprocess
import sys
"""
    A file to run commands that are used in questions on the homework
"""

# subprocess.run([])

n = len(sys.argv)
recognized_arguments = ["3a_truthful", "3a_balanced", "3b_balanced", "3b_truthful"]

if n < 2:
    print("Command-line argument needed. Try:")
    print(recognized_arguments)
    sys.exit(1)


if sys.argv[1] not in recognized_arguments:
    print("Unrecoginzed command-line argument. Try: ")
    print(recognized_arguments)
    sys.exit(1)

command = ""
if sys.argv[1] == "3a_truthful":
    command = "python3 auction.py --perms 1 --iters 200 --seed 2 Truthful,5"
elif sys.argv[1] == "3a_balanced":
    command = "python3 auction.py --perms 1 --iters 200 --seed 2 Basmbb,5"
elif sys.argv[1] == "3b_balanced":
    command = "python3 auction.py --perms 10 --iters 100 Truthful,4 Basmbb,1"
elif sys.argv[1] == "3b_truthful":
    command = "python3 auction.py --perms 10 --iters 100 Truthful,1 Basmbb,4"

subprocess.run(command.split(" "))

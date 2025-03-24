import subprocess
import sys
"""
    A file to run commands that are used in questions on the homework
"""

# subprocess.run([])

n = len(sys.argv)
recognized_arguments = ["3a_truthful", "3a_balanced", "3b_balanced", "3b_truthful", "5_cheapskate", "5_testing", "5_minbid", "5_aggro", "5_testing_perms"]

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
    command = "python3 auction.py --perms 10 --iters 200 Truthful,4 Basmbb,1"
elif sys.argv[1] == "3b_truthful":
    command = "python3 auction.py --perms 10 --iters 200 Truthful,1 Basmbb,4"
elif sys.argv[1] == "5_cheapskate":
    command = "python3 auction.py --perms 1 --iters 200 --num-rounds 48 --mech=gsp --budget 6000 BasmCheapskate,5"
elif sys.argv[1] == "5_aggro":
    command = "python3 auction.py --perms 1 --iters 200 --num-rounds 48 --mech=gsp --budget 6000 BasmAggro,5"
elif sys.argv[1] == "5_minbid":
    command = "python3 auction.py --perms 1 --iters 200 --num-rounds 48 --mech=gsp --budget 6000 BasmMinBid,5"
elif sys.argv[1] == "5_testing":
    command = "python3 auction.py --iters 100 --num-rounds 48 --mech=gsp --budget 6000 BasmCheapskate,1 BasmAggro,1 BasmMinBid,1 Truthful,1 Basmbb,1"
elif sys.argv[1] == "5_testing_perms":
    command = "python3 auction.py --perms 24 --iters 100 --num-rounds 48 --mech=gsp --budget 6000 BasmCheapskate,1 BasmAggro,1 BasmMinBid,1 Truthful,1 Basmbb,1"
subprocess.run(command.split(" "))

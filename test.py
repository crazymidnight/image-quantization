import subprocess

with open("logs.txt") as f:
    for i in range(2, 12, 2):
        for j in range(3):
            subprocess.call(["./quant", f"{i}"])

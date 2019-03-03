import subprocess


for i in range(10):
    subprocess.call(["./quant", "1"])
for i in range(2, 14, 2):
    for j in range(10):
        subprocess.call(["./quant", f"{i}"])


# Infinite loop
value = 0
while True:
    value += 1

# shell injection
import os
val = os.system("ping -c 4 127.0.0 .1; echo hacked")
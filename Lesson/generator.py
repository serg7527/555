import sys
from datetime import datetime


start = datetime.now()
print(f"Start working at: {start}")

r = range(100_000_000)

print(f"Size of object: {sys.getsizeof(r)}")
print(f"Finish at: {datetime.now()}). Working time: {datetime.now() - start}")
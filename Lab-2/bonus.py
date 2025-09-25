# Set (Hash Map) Vs List (Linear DS) #
# ---------------------------------- #
# Set Elements Are Immutable As Each Element Has A Unique Hash Value
# As Changing An Element Value Will Change Its Hash Value
# ------------------------------------------------------------------ #
import time

N = 1000000  # 1 million elements for both set and list
data_list = list(range(N))
data_set = set(range(N))
target = N - 1  # Last element

# Measure Search Time For The List
start = time.time()
found_in_list = target in data_list
end = time.time()
print(f"List search: {end - start:.6f} seconds, Found: {found_in_list}")

# Measure Search Time For The Set
start = time.time()
found_in_set = target in data_set
end = time.time()
print(f"Set search:  {end - start:.6f} seconds, Found: {found_in_set}")

import os

# Number of bytes to generate (odd number: 1,000,001)
num_bytes = 1000001  

# Generate random bytes
random_data = os.urandom(num_bytes)

# Save to a binary file
with open("odd_size.bin", "wb") as file:
    file.write(random_data)

print("Binary file 'odd_size.bin' created!")

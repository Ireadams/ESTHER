import numpy as np

# Create a 5x5 matrix with numbers from 1 to 25
matrix = np.arange(1, 26).reshape(5, 5)

print(matrix)
import numpy as np

# Create 5x5 matrix with numbers 1–25
matrix = np.arange(1, 26).reshape(5, 5)

# Create a 9x9 zero matrix to hold the diamond (rhotrix)
rhotrix = np.zeros((9, 9), dtype=int)

# Fill the rhotrix matrix diagonally
for i in range(5):
    for j in range(5):
        rhotrix[i + j, 4 - i + j] = matrix[i, j]

# Print the rhotrix matrix with zeros visible
for row in rhotrix:
    print(" ".join(f"{x:2d}" for x in row))



# Function to generate an odd-order magic square (Siamese method)
def magic_square_odd(n):
    if n % 2 == 0:
        raise ValueError("This method works only for odd n")

    # Create an empty n×n matrix
    magic = [[0] * n for _ in range(n)]

    # Starting position
    i, j = 0, n // 2

    # Fill the square
    for num in range(1, n * n + 1):
        magic[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic[new_i][new_j]:  # If already filled
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic


# Generate a 5x5 magic square
n = 5
magic_square = magic_square_odd(n)

# Print the magic square neatly
print(f"{n}x{n} Magic Square:\n")
for row in magic_square:
    print(" ".join(f"{x:2d}" for x in row))

# Check the magic constant
magic_constant = n * (n**2 + 1) // 2
print(f"\nMagic constant = {magic_constant}")




import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('mrs esther.jpg')
plt.imshow(img)
plt.axis('off')
plt.show()


img_array = np.array(img)


key = 123
encrypted_array = img_array ^ key


plt.imshow(encrypted_array)
plt.axis('off')
plt.show()


plt.imsave('encrypted_image.png', encrypted_array.astype(np.uint8))

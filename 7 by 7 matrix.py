import numpy as np

# ---------------------------------------------------------
# 1. Create a 7x7 matrix with numbers from 1 to 49
# ---------------------------------------------------------
matrix = np.arange(1, 50).reshape(7, 7)

print("7x7 Matrix (1–49):\n")
print(matrix)


# ---------------------------------------------------------
# 2. Create a 13x13 rhotrix (diamond form of the 7x7 matrix)
# ---------------------------------------------------------
rhotrix = np.zeros((13, 13), dtype=int)

# Fill the rhotrix diagonally
for i in range(7):
    for j in range(7):
        rhotrix[i + j, 6 - i + j] = matrix[i, j]

print("\n13x13 Rhotrix Matrix:\n")
for row in rhotrix:
    print(" ".join(f"{x:2d}" for x in row))


# ---------------------------------------------------------
# 3. Function to generate odd-order magic square (Siamese method)
# ---------------------------------------------------------
def magic_square_odd(n):
    if n % 2 == 0:
        raise ValueError("This method works only for odd n")

    magic = [[0] * n for _ in range(n)]
    i, j = 0, n // 2  # starting position

    for num in range(1, n * n + 1):
        magic[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n

        if magic[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic


# ---------------------------------------------------------
# 4. Generate a 7x7 magic square
# ---------------------------------------------------------
n = 7
magic_square = magic_square_odd(n)

print(f"\n{n}x{n} Magic Square:\n")
for row in magic_square:
    print(" ".join(f"{x:2d}" for x in row))

magic_constant = n * (n**2 + 1) // 2
print(f"\nMagic constant = {magic_constant}")


# ---------------------------------------------------------
# 5. Basic Image Load + XOR Encryption
# ---------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
img = mpimg.imread('mrs esther.jpg')
plt.imshow(img)
plt.axis('off')
plt.show()

# Convert to array
img_array = np.array(img)

# XOR encryption key
key = 123
encrypted_array = img_array ^ key

# Show encrypted image
plt.imshow(encrypted_array)
plt.axis('off')
plt.show()

# Save encrypted result
plt.imsave('encrypted_image.png', encrypted_array.astype(np.uint8))

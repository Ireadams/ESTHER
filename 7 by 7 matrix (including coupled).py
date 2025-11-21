import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# ---------------------------------------------------------
# 1. Create a 7x7 matrix with numbers from 1 to 49
# ---------------------------------------------------------
matrix = np.arange(1, 50).reshape(7, 7)
print("7x7 Matrix (1–49):\n", matrix)


# ---------------------------------------------------------
# 2. Create a 13×13 rhotrix (diamond layout)
# ---------------------------------------------------------
rhotrix = np.zeros((13, 13), dtype=int)

for i in range(7):
    for j in range(7):
        rhotrix[i + j, 6 - i + j] = matrix[i, j]

print("\n13×13 Rhotrix:\n")
for row in rhotrix:
    print(" ".join(f"{x:2d}" for x in row))


# ---------------------------------------------------------
# 3. Odd-order magic square (Siamese method)
# ---------------------------------------------------------
def magic_square_odd(n):
    magic = [[0] * n for _ in range(n)]
    i, j = 0, n // 2

    for num in range(1, n * n + 1):
        magic[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return np.array(magic)


magic_square = magic_square_odd(7)

print("\n7×7 Magic Square:\n")
for row in magic_square:
    print(" ".join(f"{x:2d}" for x in row))

magic_constant = 7 * (7*7 + 1) // 2
print("\nMagic Constant =", magic_constant)


# ---------------------------------------------------------
# 4. Coupled matrices (Left & Right blocks)
# ---------------------------------------------------------
def coupled_matrices(square):
    square = np.array(square)
    left = square[:, 0:4]   # columns 0–3
    right = square[:, 3:7]  # columns 3–6
    return left, right

left_coupled, right_coupled = coupled_matrices(magic_square)

print("\nLeft Coupled Matrix (7×4):\n")
for row in left_coupled:
    print(" ".join(f"{x:2d}" for x in row))

print("\nRight Coupled Matrix (7×4):\n")
for row in right_coupled:
    print(" ".join(f"{x:2d}" for x in row))


# ---------------------------------------------------------
# 5. Combine the coupled matrices (A3)
#     → horizontal merging into one 7×8 key
# ---------------------------------------------------------
combined_coupled = np.concatenate((left_coupled, right_coupled), axis=1)

# Normalize to 0–255 range
coupled_key = (combined_coupled / combined_coupled.max() * 255).astype(np.uint8)

print("\nCombined Coupled Matrix Key (7×8):\n", coupled_key)


# ---------------------------------------------------------
# 6. IMAGE ENCRYPTION PROCESS
# ---------------------------------------------------------

# ---- Load image ----
img = mpimg.imread('mrs esther.jpg')
img_array = np.array(img)

# Ensure we treat RGB or RGBA correctly
h, w = img_array.shape[:2]

# ---- Create first encryption key (7×7 matrix) ----
main_key_raw = matrix
main_key = (main_key_raw / main_key_raw.max() * 255).astype(np.uint8)

# Tile both keys to match image shape
main_key_tiled = np.tile(main_key, (h // 7 + 1, w // 7 + 1, 1))[:h, :w, :3]
coupled_key_tiled = np.tile(coupled_key, (h // 7 + 1, w // 8 + 1, 1))[:h, :w, :3]

# ---- Encryption Layer 1: XOR with main 7×7 key ----
encrypted_1 = img_array[:, :, :3] ^ main_key_tiled

# ---- Encryption Layer 2: XOR with coupled key (CM1) ----
encrypted_final = encrypted_1 ^ coupled_key_tiled

# ---- Save encrypted image ----
encrypted_image = encrypted_final.astype(np.uint8)
plt.imsave('encrypted_double_layer.png', encrypted_image)

plt.imshow(encrypted_image)
plt.axis('off')
plt.show()

print("\nEncryption Complete → File saved as: encrypted_double_layer.png")

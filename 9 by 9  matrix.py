#Encryption and decryption of a 9x9 image block using rhotrix matrix and magic square
#By Ezechi Nkiru Esther

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ============================
# STEP 1: Load image and extract 9x9 block
# ============================
# Load any image (grayscale)
image = cv2.imread("mrs esther.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Image not found! Place an image named 'mrs esther.jpg' in the working directory.")

# Resize for simplicity (ensure divisible by 9)
image = cv2.resize(image, (9, 9))
print("Original 9x9 block:")
print(image)

plt.imshow(image, cmap='gray')
plt.title("Original 9×9 Image Block")
plt.axis('off')
plt.show()

# ============================
# STEP 2: Convert to Rhotrix Matrix
# ============================
def to_rhotrix(matrix):
    """Convert a square matrix to its rhotrix (diagonal) form."""
    n = matrix.shape[0]
    rhotrix = []
    for d in range(1 - n, n):
        diag = np.diagonal(matrix, offset=d)
        rhotrix.append(list(diag))
    return rhotrix

rhotrix = to_rhotrix(image)
print("\nRhotrix (diagonal form):")
for row in rhotrix:
    print(row)

# ============================
# STEP 3: Generate a 9x9 Magic Square
# ============================
def generate_magic_square(n):
    """Generate an odd-order magic square using the Siamese method."""
    if n % 2 == 0:
        raise ValueError("Magic square generation works only for odd n.")

    magic = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    for num in range(1, n**2 + 1):
        magic[i, j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic[new_i, new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    return magic

magic_square = generate_magic_square(9)
print("\nMagic Square (9x9):\n", magic_square)

# ============================
# STEP 4: Encrypt the image block using the magic square
# ============================
def encrypt_image_block(block, magic_square):
    """Simple encryption by permuting pixels based on magic square order."""
    n = block.shape[0]
    flat_img = block.flatten()
    order = magic_square.flatten().argsort()
    encrypted_flat = flat_img[order]
    return encrypted_flat.reshape(n, n)

encrypted_block = encrypt_image_block(image, magic_square)

plt.imshow(encrypted_block, cmap='gray')
plt.title("Encrypted Image Block")
plt.axis('off')
plt.show()

# ============================
# STEP 5: Decrypt the image block
# ============================
def decrypt_image_block(block, magic_square):
    """Reverse of encrypt_image_block."""
    n = block.shape[0]
    flat_block = block.flatten()
    order = magic_square.flatten().argsort()
    decrypted = np.zeros_like(flat_block)
    decrypted[order] = flat_block
    return decrypted.reshape(n, n)

decrypted_block = decrypt_image_block(encrypted_block, magic_square)

plt.imshow(decrypted_block, cmap='gray')
plt.title("Decrypted Image Block (Should match original)")
plt.axis('off')
plt.show()

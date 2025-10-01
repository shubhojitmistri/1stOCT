# hamid_waterfall_exact_scaffold.py
# Resolution: 2000 x 1200 (m = 1..2000, n = 1..1200)
# Coordinate mapping visible under Hamid's image:
#   x = (m - 1000) / 600
#   y = (601 - n) / 600
# Output pixel = rgb( F(H0(x,y)), F(H1(x,y)), F(H2(x,y)) )

import numpy as np
from PIL import Image

W, H = 2000, 1200  # width = m_max, height = n_max

# Build m (1..W) and n (1..H) grids with broadcasting
m = np.arange(1, W + 1, dtype=np.float64)[None, :]  # shape (1, W)
n = np.arange(1, H + 1, dtype=np.float64)[:, None]  # shape (H, 1)

# Coordinate mapping (as printed under the picture)
x = (m - 1000.0) / 600.0  # shape (H, W) by broadcast
y = (601.0 - n) / 600.0

# ---------- INSERT THE EXACT FORMULAS BELOW ----------
# IMPORTANT:
#  1) Use numpy: np.sin, np.cos, np.tan, np.exp, np.log, np.sqrt, np.arctan, etc.
#  2) Products: replace \prod_{s=1}^{S} f(s) with a loop or vectorized cumulative product.
#  3) Sums: replace \sum_{s=1}^{S} f(s) with np.sum over constructed arrays.
#  4) Powers: a^b -> np.power(a, b) or a**b. Absolute value: np.abs.
#  5) Use small epsilons to avoid division by zero where needed.

def F(z):
    """
    EXACTLY copy F from the formula under the image.
    Example placeholder (DELETE and replace with the true one):
        return 255.0 * np.clip(np.exp(-z*z)*np.abs(z), 0.0, 1.0)
    """
    # -------- REPLACE THIS with Hamid's exact F(z) --------
    return 255.0 * np.clip(np.exp(-z*z)*np.abs(z), 0.0, 1.0)

# Helper examples for \sum and \prod constructs (you will use them below)
def sum_s(expr_fn, S):
    s = np.arange(1, S + 1, dtype=np.float64)
    return np.sum(expr_fn(s), axis=0)

def prod_s(expr_fn, S):
    s = np.arange(1, S + 1, dtype=np.float64)
    arr = expr_fn(s)  # shape (S, H, W) or (S, 1, 1) broadcasting to (H, W)
    return np.prod(arr, axis=0)

# Define any building-block functions exactly as printed:
# e.g., Ix(x,y), K2s(x,y), Rx(x,y), Ax(x,y), Cx(x,y), Ux(x,y), Wx(x,y), etc.
# Below are placeholders – REPLACE EVERY LINE with the true equations.

def I_s(x, y, s):
    # Placeholder; replace with the exact I_s(x,y) from the paper/image.
    return 0.0

def K_2s(x, y, s):
    # Placeholder; replace with the exact K_{2,s}(x,y).
    return 1.0

def R_x(x, y):
    # Replace with the exact R_x(x,y)
    return 0.0

def A_x(x, y):
    # Replace with the exact A_x(x,y)
    return 0.0

def C_x(x, y):
    # Replace with the exact C_x(x,y)
    return 0.0

# Example of how to implement expressions with sums/products over s:
#   \prod_{s=1}^{54} (1 - I_s(x,y))   becomes:
#       prod_term = prod_s(lambda s: (1.0 - I_s(x, y, s)) , 54)
#   \sum_{s=1}^{54} K_{2,s}(x,y)      becomes:
#       sum_term  = sum_s(lambda s: K_2s(x, y, s), 54)

def H0(x, y):
    # REPLACE this function body with the exact H_x(x,y) expression for the Red-channel preimage.
    # Use the real nested terms (R_x, A_x, C_x, I_s, K_2s, etc.) as per the printed formula.
    return 0.0

def H1(x, y):
    # REPLACE with the exact Green-channel preimage.
    return 0.0

def H2(x, y):
    # REPLACE with the exact Blue-channel preimage.
    return 0.0

# ---------- END OF FORMULA SECTION ----------

# Compute channels (vectorized over the full image)
Z0 = H0(x, y)
Z1 = H1(x, y)
Z2 = H2(x, y)

R = np.clip(F(Z0), 0.0, 255.0).astype(np.uint8)
G = np.clip(F(Z1), 0.0, 255.0).astype(np.uint8)
B = np.clip(F(Z2), 0.0, 255.0).astype(np.uint8)

img = np.dstack([R, G, B])  # (H, W, 3)
Image.fromarray(img, mode="RGB").save("waterfall_exact_2000x1200.png")
print("Saved: waterfall_exact_2000x1200.png")

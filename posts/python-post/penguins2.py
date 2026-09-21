# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "palmerpenguins>=0.1.6",
# ]
# ///
from palmerpenguins import load_penguins

penguins = load_penguins()
print(penguins.shape)
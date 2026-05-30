#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:12:44 2026

@author: hyun
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Define the number of points (M=8 for 8-PSK)
M = 8

# 2. Generate the phase angles (evenly spaced from 0 to 2*pi)
# Many implementations start at 0 or pi/M offset for specific Gray coding
angles = np.arange(0, M) * (2 * np.pi / M)

# 3. Calculate In-phase (I) and Quadrature (Q) components
I = np.cos(angles)
Q = np.sin(angles)

# 4. Create the plot
plt.figure(figsize=(6, 6))
plt.scatter(I, Q, color='blue', marker='o')

# Add labels for each constellation point (optional)
for i, (x, y) in enumerate(zip(I, Q)):
    print(i,f"{x:.2f}",f"{y:.2f}j")
    plt.text(x * 1.1, y * 1.1, f'{i:03b}', fontsize=12, ha='center')

# Aesthetic improvements
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.title('8-PSK Constellation Diagram')
plt.xlabel('In-phase (I)')
plt.ylabel('Quadrature (Q)')
plt.axis('equal')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()
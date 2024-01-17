import numpy as np
import matplotlib.pyplot as plt

# 복소수 생성
z = 1 + 2j

# 실수부와 허수부 분리
real_part = z.real
imag_part = z.imag

# 그래프 그리기
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, real_part, imag_part, angles='xy', scale_units='xy', scale=1, color='blue')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.title('Complex Number: {} + {}j'.format(real_part, imag_part))
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

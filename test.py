import numpy as np
import matplotlib.pyplot as plt

# theta 값을 0부터 4π까지 균일하게 생성
theta = np.linspace(0, 4 * np.pi, 1000)
r = 1 + np.sin(theta / 2)

# 극좌표 플롯
plt.figure(figsize=(6,6))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_title(r'$r = 1 + \sin(\frac{\theta}{2})$ 의 극좌표 그래프', va='bottom')
plt.show()
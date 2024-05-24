import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return x ** 2
a = 0  
b = 2  
def monte_carlo_integration(f, a, b, num_samples):
    samples = np.random.uniform(a, b, num_samples)
    sample_values = f(samples)
    integral_estimate = (b - a) * np.mean(sample_values)
    return integral_estimate
num_samples = 10000
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)
analytical_result, _ = quad(f, a, b)
print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Аналітичний розрахунок (quad): {analytical_result}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

import matplotlib.pyplot as plt
import os

fig_dir = os.path.join(os.getcwd(), '..', 'src', 'figures')

fig = plt.figure(figsize=(3,3))
plt.plot([2, 3, 5], [1, 2, 3])
plt.tight_layout()

plt.savefig(os.path.join(fig_dir, 'example.png'))
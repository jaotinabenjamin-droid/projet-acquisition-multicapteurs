import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Paramètres
duree = 10
fs_temp = 1
fs_press = 5
fs_vib = 20

# Temps
t_temp = np.arange(0, duree, 1 / fs_temp)
t_press = np.arange(0, duree, 1 / fs_press)
t_vib = np.arange(0, duree, 1 / fs_vib)

# Simulation
temp = 25 + 2 * np.sin(0.5 * t_temp)
press = 1 + 0.5 * np.sin(2 * t_press)
vib = 0.2 * np.sin(10 * t_vib)

# Synchronisation
t_common = np.linspace(0, duree, 200)
temp_sync = np.interp(t_common, t_temp, temp)
press_sync = np.interp(t_common, t_press, press)
vib_sync = np.interp(t_common, t_vib, vib)

# Sauvegarde
df = pd.DataFrame({
    "Temps": t_common,
    "Température": temp_sync,
    "Pression": press_sync,
    "Vibration": vib_sync
})

df.to_csv("data.csv", index=False)

# Graphiques
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t_common, temp_sync)
plt.title("Température synchronisée")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t_common, press_sync)
plt.title("Pression synchronisée")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_common, vib_sync)
plt.title("Vibration synchronisée")
plt.grid(True)

plt.tight_layout()
plt.show()

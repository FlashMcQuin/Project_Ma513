import numpy as np
from matplotlib import pyplot as plt
import random
data = np.load('images_malware.npz', allow_pickle=True)
print(type(data))
lst = data.files
image_data = data['arr']
fig, axes = plt.subplots(2, 4, figsize=(16, 6), label = "Malware Images")

# Flatten the 2D array of axes to make indexing easier
axes = axes.flatten()

family_dict = { 1 :["Dialer", "Adialer.C", 122],
2 :["Backdoor", "Agent.FYI", 116],
3 :["Worm", "Allaple.A", 2949],
4: ["Worm", "Allaple.L", 1591],
5 :["Trojan", "Alueron.gen!J", 198],
6 :["Worm:AutoIT", "Autorun.K", 106],
7 :["Trojan", "C2Lop.P", 146],
8 :["Trojan", "C2Lop.gen!G", 200],
9 :["Dialer", "Dialplatform.B", 177],
10 :["Trojan Downloader", "Dontovo.A", 162],
11 :["Rogue", "Fakerean", 381],
12 :["Dialer", "Instantaccess", 431],
13 :["PWS", "Lolyda.AA", 1213],
14 :["PWS", "Lolyda.AA", 2184],
15 :["PWS", "Lolyda.AA", 3123],
16 :["PWS", "Lolyda.AT", 159],
17 :["Trojan", "Malex.gen!J", 136],
18 :["Trojan Downloader", "Obfuscator.AD", 142],
19 :["Backdoor", "Rbot!gen", 158],
20 :["Trojan", "Skintrim.N", 80],
21 :["Trojan Downloader", "Swizzor.gen!E", 128],
22 :["Trojan Downloader", "Swizzor.gen!I", 132],
23 :["Worm", "VB.AT", 408],
24 :["Trojan Downloader", "Wintrim.BX", 97],
25 :["Worm", "Yuner.A ",800]}

random_indices = random.sample(range(image_data.shape[0]), 8)

for i, index in enumerate(random_indices):
    img1, family = image_data[index]
    axes[i].imshow(img1, cmap='gray')
    axes[i].set_title(f"family : {family_dict[family+1][0]} \nname : {family_dict[family+1][1]}")
    axes[i].axis('off') 
plt.show()
"""
x_coordinates = image_data[:, 0]
y_coordinates = image_data[:, 1]

# Create a scatter plot
plt.scatter(x_coordinates, y_coordinates, s=1)  # Adjust 's' for point size
plt.title('Scatter Plot of Image Points')
plt.show()"""



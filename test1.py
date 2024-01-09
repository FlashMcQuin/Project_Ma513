import numpy as np
from matplotlib import pyplot as plt

data = np.load('images_malware.npz', allow_pickle=True)
print(type(data))
lst = data.files
print(lst)
print(type(lst))
image_data = data['arr']
fig, axes = plt.subplots(2, 3, figsize=(10, 6))

# Flatten the 2D array of axes to make indexing easier
axes = axes.flatten()
print(image_data.shape)
for i, img in enumerate(image_data[:6]):
    img1, family = img
    axes[i].imshow(img1, cmap='gray')
    axes[i].set_title(family)  # You can specify the colormap as needed
    axes[i].axis('off') 
    #plt.imshow(img1, 'gray')

plt.show()
"""
x_coordinates = image_data[:, 0]
y_coordinates = image_data[:, 1]

# Create a scatter plot
plt.scatter(x_coordinates, y_coordinates, s=1)  # Adjust 's' for point size
plt.title('Scatter Plot of Image Points')
plt.show()"""



from PIL import Image
import numpy as np
import pandas as pd

def extract_areas_with_color(image_path, target_color):
    """
    Extracts areas with a specified color from a PNG image.
    
    Parameters:
        image_path (str): Path to the input PNG image.
        target_color (tuple): The target color (R, G, B, A) or (R, G, B) to extract.
    
    Returns:
        np.ndarray: A binary mask where 1 indicates matching color areas.
    """
    # Load the image
    image = Image.open(image_path).convert("RGBA")  # Ensure RGBA mode
    
    # Convert image to NumPy array
    img_array = np.array(image)
    
    # Create a boolean mask where pixels match the target color
    color_mask = (img_array[..., :len(target_color)] == target_color).all(axis=-1)
    
    # Convert the mask to integers for visualization or further processing
    binary_mask = color_mask.astype(np.uint8)
    
    return binary_mask

def extract_areas_with_color_import_array(img_array, target_color):
    # Create a boolean mask where pixels match the target color
    color_mask = (img_array[..., :len(target_color)] == target_color).all(axis=-1)
    
    # Convert the mask to integers for visualization or further processing
    binary_mask = color_mask.astype(np.uint8)
    
    return binary_mask

#directory = "Matsuura_2015"
#image_path = f"{directory}//map_code.png"  # Replace with your PNG file path

map_image = "Yonekura_1966//Fig4-2//4-2_code"
image_path = f"{map_image}.png"

color_codes = f"work//color_code.dat"
# Load the data into a DataFrame
df = pd.read_csv(
    color_codes,
    sep=',',        # Specify tab as the delimiter
    comment='#',     # Skip lines starting with '#'
    na_values='NaN'  # Treat 'NaN' as missing values
)
num_rows = df.shape[0]

MIS_list = df["MIS"].tolist()
# Load the image
image = Image.open(image_path).convert("RGBA")  # Ensure RGBA mode
    
# Convert image to NumPy array
img_array = np.array(image)
    
for MIS in MIS_list:
    target_color = df.loc[df["MIS"] == MIS, ["R", "G", "B", "A"]].iloc[0].tolist()
    
    binary_mask = extract_areas_with_color_import_array(img_array, target_color)
    
    if np.all(binary_mask == 0):
        print(f"no {MIS} terrace")
    else:
        export_file = f"{map_image}_{MIS}.png"
        #Image.fromarray(binary_mask * 255).save(export_file)
        Image.fromarray((1-binary_mask) * 255).save(export_file)
        print(f"{MIS} terrace exported to {export_file}")
    
'''
# Visualize the mask (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.imshow(binary_mask, cmap="gray")
plt.title("Extracted Areas with Specified Color")
plt.axis("off")
plt.show()
'''
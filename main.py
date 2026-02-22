from PIL import Image

# IMPORTANT: Update these file paths to match your local directory structure
# Replace the paths below with the actual location of your files on your computer

# Path to the image you want to place on the template
image1 = Image.open("D:\CodingShenanigans\Makoters/TheImage.png")

# Path to the template image
image2 = Image.open("D:\CodingShenanigans\Makoters/Template.jpg")

# Convert both images to RGBA format for transparency support
imagea = image1.convert("RGBA")
imageb = image2.convert("RGBA")

# Resize the image to fit the template (adjust dimensions as needed)
img = imagea.resize((766,487))

# Create a new image with the same size as the template
final = Image.new("RGBA", imageb.size, (0, 0, 0, 0))

# Paste the resized image onto the template at position (54, 637)
# Adjust these coordinates to change where the image is placed on the template
final.paste(img, (54, 637), mask=img)

# Composite the template over the final image
final = Image.alpha_composite(final, imageb)

# Save the result - IMPORTANT: Update this path to where you want to save the output file
final.save("D:\CodingShenanigans\Makoters/Result.png")
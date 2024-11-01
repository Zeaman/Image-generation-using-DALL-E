from PIL import Image

# Re-attempt resizing the previously generated celestial image
image_path_celestial = "/mnt/data/A_realistic_image_of_the_night_sky_filled_with_cel.png"
output_resized_celestial_path = "/mnt/data/space_celestial_424x464.webp"

# Open the image
image_celestial = Image.open(image_path_celestial)

# Resize the image to 424x464 pixels
resized_image_celestial = image_celestial.resize((424, 464))

# Save the resized image in the specified format
resized_image_celestial.save(output_resized_celestial_path, format="WEBP")
output_resized_celestial_path

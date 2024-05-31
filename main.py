from PIL import Image

# Open and convert images
legend = Image.open(r"./images/legend.png").convert("RGBA")
land = Image.open(r"./images/land.png").convert("RGBA")
topography = Image.open(r"./images/topography.png").convert("RGBA")
weather = Image.open(r"./images/weather.png").convert("RGBA")
locations = Image.open(r"./images/locations.png").convert("RGBA")
range = Image.open(r"./images/range.png").convert("RGBA")
copyright = Image.open(r"./images/copyright.png").convert("RGBA")

# Create a base image with the same size as the legend image
base_image = Image.new("RGBA", legend.size, (0, 0, 0, 0))

# Paste the smaller images onto the base image
base_image.paste(legend, (0, 0))
base_image.paste(land, (0, 0), mask=land)
base_image.paste(topography, (0, 0), mask=topography)
base_image.paste(weather, (0, 0), mask=weather)
base_image.paste(locations, (0, 0), mask=locations)
base_image.paste(range, (0, 0), mask=range)
base_image.paste(copyright, (0, 0), mask=copyright)

# Save the final image
base_image.save("final.png")

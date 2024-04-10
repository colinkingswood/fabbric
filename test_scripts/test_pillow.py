from PIL import Image

def apply_color_to_grayscale_image(image_path, color):
    # Load the image in grayscale mode
    grayscale_image = Image.open(image_path).convert('L')

    # Convert the grayscale image back to RGB
    colored_image = grayscale_image.convert('RGB')

    # Apply the color to the image
    colored_pixels = [(int(pixel * color[0] / 255), int(pixel * color[1] / 255), int(pixel * color[2] / 255))
                      for pixel in grayscale_image.getdata()]
    colored_image.putdata(colored_pixels)

    return colored_image

# Usage
image_path = '../data/Regular_5cm_TankTop_0.png'
color = (0, 0, 255)  # Blue color
colored_image = apply_color_to_grayscale_image(image_path, color)
colored_image.show()

from PIL import Image, ImageColor


def change_color(image_path, hexcolor):
    """
    This will take an image, we are assuming a white / greyscale transparent png
    and apply the hexcolor to it

    :param image_path:
    :param hexcolor:
    :return: A pillow Image with teh color adjusted
    """
    color = ImageColor.getcolor(hexcolor, "RGB")
    # Load the image
    image = Image.open(image_path)

    # Separate the alpha channel
    alpha_channel = image.split()[-1] if image.mode == 'RGBA' else None

    # Convert the image to grayscale and then back to RGB
    grayscale_image = image.convert('L')
    colored_image = grayscale_image.convert('RGB')

    # Apply the color to the image
    colored_pixels = [(int(pixel * color[0] / 255), int(pixel * color[1] / 255), int(pixel * color[2] / 255))
                      for pixel in grayscale_image.getdata()]
    colored_image.putdata(colored_pixels)

    # Combine the colored image with the alpha channel
    if alpha_channel:
        colored_image.putalpha(alpha_channel)

    return colored_image


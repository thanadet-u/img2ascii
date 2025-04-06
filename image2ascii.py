from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# ASCII characters from lightest to darkest
ASCII_CHARS = [" ", ".", ":", "c", "o", "P", "O", "?", "@", "█"]


# Reverse list (inverted color)
R_ASCII_CHARS = ["█", "@", "?", "O", "P", "o", "c", ":", ".", " "]

# Set character size
CHAR_WIDTH = 8
CHAR_HEIGHT = 8

#SET font path (we are using a 8x8 pixel font to make keep the images dimensions)
FONT_PATH = "./MxPlus_IBM_BIOS.ttf"


'''
Basic image to ascii conversation using the difference in luminance
'''
def resize_image(image):
    # Resize image while maintaining aspect ratio.
    width, height = image.size
    aspect_ratio = height / width
    new_width = int(width // CHAR_WIDTH)
    new_height = int(new_width * aspect_ratio)
    return image.resize((new_width, new_height))

def brightness_to_ascii(brightness):
    # calulate the brightness and return a character
    index = int(brightness / 255 * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[index]

def convert_ascii(image):
    # Convert image to ASCII characters.
    pixels = np.array(image.convert("L"))  # Ensure it's grayscale
    height, width = pixels.shape
    ascii_image = []

    for y in range(height):
        line = "".join(brightness_to_ascii(pixels[y, x]) for x in range(width))
        ascii_image.append(line)

    return ascii_image

def save_ascii_as_image(ascii_art ,bg ,char_c, output_path="ascii_image.png"):
    # Render ASCII art as an image
    font = ImageFont.truetype(FONT_PATH, CHAR_HEIGHT)
    img_width = len(ascii_art[0]) * CHAR_WIDTH
    img_height = len(ascii_art) * CHAR_HEIGHT

    img = Image.new("RGB", (img_width, img_height), bg)  # Background color
    draw = ImageDraw.Draw(img)

    for i, line in enumerate(ascii_art):
        draw.text((0, i * CHAR_HEIGHT), line, font=font, fill=char_c)  # Char color

    img.save(output_path)
    print(f"ASCII art saved as {output_path}")


def main():
    path = input("Enter path to image: ")

    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Error: {e}")
        return

    # color_scheme = input("Choose color options [monochrome: m, color: c]: ").strip().lower()
    color_scheme = input("Choose color scheme[Black/White: BW, Pink: P, Blue: B, Green: G]").strip().lower()

    image = resize_image(image)
    ascii_art = convert_ascii(image)

    for line in ascii_art:
        print(line)

    filename, _ = os.path.splitext(os.path.basename(path))
    output_path = f"{filename}_{color_scheme}_ascii.png"

    if color_scheme in ["bw", "blackwhite","black white", "black and white"]:
        save_ascii_as_image(ascii_art, "black", "white", output_path)
    elif color_scheme in ["p", "pink"]:
        save_ascii_as_image(ascii_art, "#303446", "#eebebe", output_path)
    elif color_scheme in ["blue", "b"]:
        save_ascii_as_image(ascii_art, "#002D62", "#88C0D0", output_path)
    elif color_scheme in ["green", "g"]:
        save_ascii_as_image(ascii_art, "black", "#03A062", output_path)

    with open("ascii_image.txt", "w") as f:
        f.write("\n".join(ascii_art))

if __name__ == "__main__":
    main()

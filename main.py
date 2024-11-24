import PIL.Image

# ASCII character set to map pixel values (from light to dark)
ASCII_CHARS = " .,o'-~+i:;?>='*^0#&%$@"

def resize_image(image, new_width=100):
    """
    Resize the image while maintaining aspect ratio.
    
    Args:
        image (PIL.Image): The input image.
        new_width (int): The desired width of the output image.
    
    Returns:
        PIL.Image: The resized image.
    """
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    return image.resize((new_width, new_height))

def gray_image(image):
    """
    Convert the image to grayscale.
    
    Args:
        image (PIL.Image): The input image.
    
    Returns:
        PIL.Image: Grayscale image.
    """
    return image.convert("L")

def pixels_to_ascii(image):
    """
    Map each pixel value to an ASCII character based on intensity.
    
    Args:
        image (PIL.Image): Grayscale image.
    
    Returns:
        str: A string of ASCII characters representing the image.
    """
    pixels = image.getdata()
    scale_factor = 256 / len(ASCII_CHARS)
    return "".join([ASCII_CHARS[int(pixel // scale_factor)] for pixel in pixels])

def convert_image_to_ascii(path, new_width=100):
    """
    Convert an image to ASCII art.
    
    Args:
        path (str): Path to the input image file.
        new_width (int): Desired width of the ASCII art.
    
    Returns:
        str: The ASCII art representation of the image.
    """
    try:
        image = PIL.Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' not found.")
    except PIL.UnidentifiedImageError:
        raise ValueError(f"File '{path}' is not a valid image.")
    
    image = resize_image(image, new_width)
    image = gray_image(image)
    ascii_art = pixels_to_ascii(image)
    pixel_count = len(ascii_art)
    return "\n".join(ascii_art[i:i+new_width] for i in range(0, pixel_count, new_width))

def main():
    path = input("Write a valid path for the image: ")
    try:
        new_width = int(input("Enter desired width for ASCII art (default 100): ") or 100)
    except ValueError:
        print("Invalid width! Using default value of 100.")
        new_width = 100

    try:
        ascii_art = convert_image_to_ascii(path, new_width)
    except FileNotFoundError as e:
        print(e)
        return
    except ValueError as e:
        print(e)
        return

    output_file = "ascii_image.txt"
    with open(output_file, "w") as f:
        f.write(ascii_art)

    print(f"ASCII art saved to '{output_file}'.")
    display = input("Display ASCII art in console? (y/n): ").strip().lower()
    if display.lower() == "y":
        print("\n" + ascii_art)

if __name__ == "__main__":
    main()

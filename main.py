import PIL.Image

# Mais caracteres para melhor definição (do claro ao escuro)
ASCII_CHARS = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def resize_image(image, new_width=100):
    """
    Redimensiona a imagem mantendo a proporção.
    """
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    return image.resize((new_width, new_height))

def gray_image(image):
    """
    Converte a imagem para escala de cinza.
    """
    return image.convert("L")

def convert_image_to_ascii(path, new_width=100, colored=True):
    """
    Converte uma imagem em arte ASCII (mantendo a proporção original e adicionando cor RGB).
    """
    try:
        image = PIL.Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' not found.")
    except PIL.UnidentifiedImageError:
        raise ValueError(f"File '{path}' is not a valid image.")

    image = resize_image(image, new_width)
    gray = gray_image(image)
    color_img = image.convert("RGB")

    pixels_gray = list(gray.getdata())
    pixels_color = list(color_img.getdata())

    scale_factor = 256 / len(ASCII_CHARS)
    ascii_art_lines = []

    for y in range(image.height):
        line = ""
        for x in range(image.width):
            i = y * image.width + x
            gray_val = pixels_gray[i]
            r, g, b = pixels_color[i]
            char = ASCII_CHARS[int(gray_val // scale_factor)]
            if colored:
                line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            else:
                line += char
        ascii_art_lines.append(line)

    return "\n".join(ascii_art_lines)

def main():
    path = input("Write a valid path for the image: ")
    try:
        new_width = int(input("Enter desired width for ASCII art (default 100): ") or 100)
    except ValueError:
        print("Invalid width! Using default value of 100.")
        new_width = 100

    color_choice = input("Show colors in console? (y/n): ").strip().lower()
    colored = (color_choice == "y")

    try:
        ascii_art = convert_image_to_ascii(path, new_width, colored)
    except FileNotFoundError as e:
        print(e)
        return
    except ValueError as e:
        print(e)
        return

    output_file = "ascii_image_colored.txt" if colored else "ascii_image.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        if colored:
            import re
            ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
            f.write(ansi_escape.sub('', ascii_art))  # remove cores ao salvar
        else:
            f.write(ascii_art)

    print(f"ASCII art saved to '{output_file}'.")
    display = input("Display ASCII art in console? (y/n): ").strip().lower()
    if display == "y":
        print("\n" + ascii_art)

if __name__ == "__main__":
    main()

# ImageToAscii

**ImageToAscii** is a Python script that converts any image into ASCII art. It uses the `Pillow` library to process images and map their pixel intensities to an ASCII character set.

## How It Works

1. **Image Resizing**: The image is resized proportionally to fit the desired width.
2. **Grayscale Conversion**: Each pixel is converted to a grayscale intensity value.
3. **ASCII Mapping**: The intensity values are mapped to a set of ASCII characters (from darkest to lightest).
4. **Output**: The result is saved as a `.txt` file and can optionally be displayed in the console.

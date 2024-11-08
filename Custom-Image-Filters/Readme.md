# Image Processing with Custom Filters

This Python project provides basic image processing techniques, including applying grayscale and custom filters, scaling images, and cropping images. The code makes use of NumPy and a custom filter function to manipulate images in various ways.

## Features

- **Gray Scaled Filter**: Converts an image to grayscale using the standard RGB-to-grayscale formula.
- **Custom Filter**: A custom filter that changes the color channels of an image (RGB to BRG).
- **Image Scaling**: Resizes an image by scaling its width and height by specified factors.
- **Image Cropping**: Crops a specified region from an image.

## Getting Started

### Prerequisites

- **Python 3.x**
- **NumPy library**
- **Pillow (PIL) library** for image loading and displaying

Install required libraries using:
```bash
pip install numpy pillow
```
## Running Code
- Clone this repository or copy the code into a Python file (e.g., image_processing.py).
- Ensure you have an image file (e.g., pic.jpg) in the same directory or modify the get_input() function to specify the path to your image.
- Open a terminal, navigate to the file location, and run:
  ```bash
  python image_processing.py
  ```
## Input and Output:
The script will display the following outputs:
  - Input Image: Displays the original image.
  - Gray Scaled: Converts and displays the grayscale version of the image.
  - Custom Filter: Applies a custom filter to the image and displays the result.
  - Inverted Custom Filter: Applies the inverse of the custom filter and displays the result.
  - Cropped Image: Displays a cropped version of the image, based on the specified coordinates.
  - Scaled Image: Displays a scaled version of the image based on the width and height scaling factors.
## Image Processing Functions:
1. grayScaledFilter(img):
    - Converts the input image to grayscale using the formula Gray = 0.2989*R + 0.5870*G + 0.1140*B.
2. customFilter(img):
    - Applies a custom filter that changes the color channels of an image (from RGB to BRG).
      Also shows the image after applying the inverse of the custom filter.
3. scaleImg(img, scale_width, scale_height):
    - Scales the image by specified width and height factors.
4. cropImg(img, start_row, end_row, start_column, end_column):
    - Crops the image to a specified rectangular region based on row and column indices.


## License
This project is open-source and available for use under the [MIT License](https://opensource.org/licenses/MIT).

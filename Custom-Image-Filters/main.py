from utils import *
import numpy as np

def grayScaledFilter(img):
    filter = np.array([[0.2989, 0.5870, 0.1140]])
    return Filter(img, filter)

# changes image from RGB mode to BRG mode
def customFilter(img):
    filter_matrix = np.array([[0, 0, 1],
                              [0, 1, 0],
                              [1, 0, 0]])
    inv = np.linalg.inv(filter_matrix)
    res = Filter(img, filter_matrix)
    return res, Filter(res, inv)


def scaleImg(img, scale_width, scale_height):
    number_rows = scale_width * len(img)
    number_columns = scale_height * len(img[0])
    dst = np.zeros((number_rows, number_columns, img.shape[2]))

    for i in range(number_rows):
        for j in range(number_columns):
            dst[i, j] = img[int(i / scale_width), int(j / scale_height)]

    return dst


def cropImg(img, start_row, end_row, start_column, end_column):
    res = np.zeros(shape=(end_row - start_row + 1, end_column - start_column + 1, 3))
    for i in range(start_row, end_row):
        for j in range(start_column, end_column):
            res[i - start_row, j - start_column] = img[i, j]
    return res


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    grayScalePic = grayScaledFilter(image_matrix)
    showImage(grayScalePic, title="Gray Scaled")

    customFilteredImage, inverted = customFilter(image_matrix)
    showImage(customFilteredImage, title="Custom")
    showImage(inverted, title="Inverted Custom")

    croppedImage = cropImg(image_matrix, 80, 500, 80, 425)
    showImage(croppedImage, title="Cropped Image")

    scaledImage = scaleImg(image_matrix, 2, 3)
    showImage(scaledImage, title="Scaled Image")

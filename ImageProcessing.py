import math
def rgb_to_gray(image):
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    gray = 0.21 * red + 0.71 * green + 0.07 * blue
    return gray
def negative(image):
    result = []
    for i in range(len(image)):
        total = 0
        total += 1 - image[i]
        result.append(total)
    return result
def log_transformation(image):
    max_value = 255
    c = max_value / (math.log(max_value+1))
    result = []
    for image_row in image:
        result_row = []
        for pixel in image_row:
            result_pixel = []
            for i, color in enumerate(pixel):
                if color != 0 and i != 3:
                    result_pixel.append(round(math.log10(round(color * 255)) * c))
                else:
                    result_pixel.append(int(color) * 255)
            result_row.append(result_pixel)
        result.append(result_row)
    return result

from PIL import Image
import numpy as np

bayer_array = np.array([    ['G', 'B'],
                            ['R', 'G']      ])

fuji_array = np.array([     ['G', 'B', 'R', 'G', 'R', 'B'],
                            ['R', 'G', 'G', 'B', 'G', 'G'],
                            ['B', 'G', 'G', 'R', 'G', 'G'],
                            ['G', 'R', 'B', 'G', 'B', 'R'],
                            ['B', 'G', 'G', 'R', 'G', 'G'],
                            ['R', 'G', 'G', 'B', 'G', 'G'],     ])

def to_mosaic(image, window):
    mosaic = image.copy()
    for i in range(0, image.shape[0]-window.shape[0]+1, window.shape[0]):
        for j in range(0, image.shape[1]-window.shape[1]+1, window.shape[1]):
            for k in range(window.shape[0]):
                for l in range(window.shape[1]):
                    if window[k, l] == 'R':
                        mosaic[i+k, j+l, 1] = 0
                        mosaic[i+k, j+l, 2] = 0
                    elif window[k, l] == 'G':
                        mosaic[i+k, j+l, 0] = 0
                        mosaic[i+k, j+l, 2] = 0
                    elif window[k, l] == 'B':
                        mosaic[i+k, j+l, 0] = 0
                        mosaic[i+k, j+l, 1] = 0
    return mosaic


def to_demosaic(mosaic, window):
    demosaic = mosaic.copy()
    for i in range(0, mosaic.shape[0]-window.shape[0]+1, window.shape[0]):
        for j in range(0, mosaic.shape[1]-window.shape[1]+1, window.shape[1]):
            r, g, b = 0, 0, 0
            r_count, g_count, b_count = 0, 0, 0
            for k in range(window.shape[0]):
                for l in range(window.shape[1]):
                    r_count += 1 if window[k, l] == 'R' else 0
                    g_count += 1 if window[k, l] == 'G' else 0
                    b_count += 1 if window[k, l] == 'B' else 0
                    r += mosaic[i+k, j+l, 0]
                    g += mosaic[i+k, j+l, 1]
                    b += mosaic[i+k, j+l, 2]
            
            for k in range(window.shape[0]):
                for l in range(window.shape[1]):
                  demosaic[i + k, j + l] = [r / r_count, g / g_count, b / b_count]
    return demosaic


def img_to_array(file):
    return np.asarray(Image.open(file))

def array_to_img(array, file):
    (Image.fromarray(array)).save(file)

def main():
    image = img_to_array('jan_pat.jpg')
    mosaic = to_mosaic(image, bayer_array)
    demosaic = to_demosaic(mosaic, bayer_array)

    array_to_img(mosaic, 'jan_pat_mosaic.png')
    array_to_img(demosaic, 'jan_pat_demosaic.png')
    

main()
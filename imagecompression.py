import numpy as np
from PIL import Image

def compress_image(image_path, compression_ratio):

    img = Image.open(image_path)
    img_array = np.array(img)

    U, S, Vt = np.linalg.svd(img_array, full_matrices=False)

    k = int(compression_ratio * min(img_array.shape[:-1]))

    compressed_img_array = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

    compressed_img_array = np.uint8(compressed_img_array)
    compressed_img = Image.fromarray(compressed_img_array)

    return compressed_img

if __name__ == "__main__":
    image_path = "/home/indrajeetyadav/Desktop/maths assignment final/Screenshot from 2023-12-30 17-15-37.png"

    compression_ratio = 0.1

    compressed_img = compress_image(image_path, compression_ratio)
    compressed_img.show()

import matplotlib

import matplotlib.pyplot as plt



def get_bar_values():
    matplotlib.use("TkAgg")
    img = plt.imread("IMG_1032.JPG")
    y_values = [70, 195, 323]
    ivs = []
    for y in y_values:

        if 100 < img[y][250][2] < 150:
            ivs.append(15)
            continue
        orange_count = 0
        count = 0
        for pixel in img[y][35:470]:
            if pixel[0] > 230:
                orange_count += 1

            count += 1

        ivs.append((int(15 * orange_count / count)))
    return ivs


#plt.imshow(img)
#plt.axis("off")
#plt.show()
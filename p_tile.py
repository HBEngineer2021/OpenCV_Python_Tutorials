import cv2
import argparse
import urllib.request
import pathlib
import numpy as np
import matplotlib.pyplot as plt

def main():
    # URLから画像をparse出来る様に設定。
    parser = argparse.ArgumentParser()
    #parser.add_argument('-u', '--url',default='https://github.com/HBEngineer2021/OpenCV_Python_Tutorials/blob/main/img/date_a_live_10th.png?raw=true')
    parser.add_argument('-s', '--save_file_name', default='../kivy_opencv/img/utawarerumono.jpg')
    #parser.add_argument('-r', '--ratio', type=float, default=0.07)
    #parser.add_argument('-mi', '--min', type=int, default=80)
    #parser.add_argument('-ma', '--max', type=int, default=200)
    arguments = parser.parse_args()

    # parseした画像を読み込み設定
    '''if not pathlib.Path(arguments.save_file_name).exists():
        print('Downloading ...', end=' ')
        urllib.request.urlretrieve(arguments.url, filename=arguments.save_file_name)
        print('Done.')'''

    # 画僧を読み込む
    image = cv2.imread(arguments.save_file_name, cv2.IMREAD_GRAYSCALE)
    histogram, bins = np.histogram(image.ravel(), 256, [0, 256], density=True)
    """cdf = np.cumsum(histogram)
    for x, p in enumerate(cdf):
        if p > arguments.ratio:
            threshold = x
            break
    print(f'threshold: {threshold}')
    ret, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)"""

    """threshold = histogram[arguments.min:arguments.max].argmin() + arguments.min
    print(f'threshold: {threshold}')
    ret, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)"""
    ret, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print(f'threshold: {ret}')

    fig = plt.figure(figsize=(6.4, 4.8 / 2))
    ax = fig.add_subplot()
    x = np.arange(256)
    ax.bar(x, histogram)
    #ax.vlines(threshold, ymin=0, ymax=histogram.max(), colors='red')
    ax.vlines(ret, ymin=0, ymax=histogram.max(), colors='red')
    ax.set_xlabel('intensity')
    #ax.vlines(arguments.min, ymin=0, ymax=histogram.max(), colors='green', linestyles='dashed')
    #ax.vlines(arguments.max, ymin=0, ymax=histogram.max(), colors='green', linestyles='dashed')
    #ax.set_ylabel('ratio')
    ax.set_title('Fig.1: Histogram of grayscale image.')
    ax.grid(color='black', linestyle='dotted', axis='y')
    ax.set_axisbelow(True)
    plt.show()

    cv2.imshow('input image', image)
    cv2.imwrite("../kivy_opencv/img/input image.jpg", image)
    cv2.imshow('binary image', binary_image)
    cv2.imwrite("../kivy_opencv/img/binary image2.jpg", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
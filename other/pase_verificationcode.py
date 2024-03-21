# -*- coding: utf-8 -*-

import ddddocr
import requests

from kew_word.kewword import *

def parse_yanzheng(path):
    """

    :param path: 验证码图片文件路径
    :return:
    """
    # 识别验证码
    ocr = ddddocr.DdddOcr(beta=True, show_ad=False)
    with open(path, 'rb') as f:
        image = f.read()

    res = ocr.classification(image)
    print("验证码识别结果：{}".format(res))
    return res


if __name__ == '__main__':
    print(parse_yanzheng('url-formal'))

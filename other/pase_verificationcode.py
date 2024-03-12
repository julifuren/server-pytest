# -*- coding: utf-8 -*-

import ddddocr
import requests

from kew_word.kewword import *


def parse_yanzheng(biaoshi):
    # 定义接口URL
    if biaoshi == 'url-dev':
        url = 'https://engine-dev.piesat.cn/bpaas/janus/gateway/api'
        # 如果需要传递POST请求的数据，可以在这里定义
        payload = {'action': 'PWDLOGIN', 'sendType': 'WEB'}  # 根据需要添加POST请求的数据
        # 定义请求头
        headers = {
            'x-api': 'engine.login.getGraphCaptcha',
            'x-app': 'rPvyWAC0cvfT66TH1UbO',
            'x-client': 'WEB',
            'x-gw-version': '2',
            'x-host-app-id': 'engine',
            'x-language': 'zh_CN',
            'x-nonce': 'd03db910-529c-4dae-b07d-7ecade9f9b84',
            'x-sign': '50b8d8cfcb8f8f08bdd08c5288f5598e',
            'x-stage': 'TEST',
            'x-ts': '1704424071325',
        }
        # 发送POST请求
        response = requests.post(url, json=payload, headers=headers)

        # 检查请求是否成功
        if response.status_code == 200:
            # 获取图片内容
            image_data = response.content

            file_name = os.path.join(get_project_path(), 'other')
            # 指定保存的文件名和路径
            filename = file_name + "\\" + 'yzm.jpg'  # 可以根据需要修改文件名和扩展名

            # 使用二进制写入模式保存图片
            with open(filename, 'wb') as file:
                file.write(image_data)

            # 识别验证码
            ocr = ddddocr.DdddOcr(beta=True, show_ad=False)
            print(filename)
            with open(filename, 'rb') as f:
                image = f.read()

            res = ocr.classification(image)
            print("验证码识别结果：{}".format(res))
            return res

        else:
            print('请求失败')
            print(response.status_code)
            print(response.text)

    elif biaoshi == 'url-formal':
        url = 'https://janus.piesat.cn/gateway/api'  # 替换成你的接口URL
        # 如果需要传递POST请求的数据，可以在这里定义
        payload = {'action': 'PWDLOGIN', 'sendType': 'WEB'}  # 根据需要添加POST请求的数据
        # 定义请求头
        headers = {
            'x-api': 'engine.login.getGraphCaptcha',
            'x-app': 'rPvyWAC0cvfT66TH1UbO',
            'x-client': 'WEB',
            'x-gw-version': '2',
            'x-host-app-id': 'engine',
            'x-language': 'zh_CN',
            'x-nonce': '99a14f90-bb3a-4099-a191-a9fadd4b2756',
            'x-sign': 'd8f4e2a9080b4e1aa8306d6ec521d784',
            'x-stage': 'PROD',
            'x-ts': '1696748451856',
        }
        # 发送POST请求
        response = requests.post(url, json=payload, headers=headers)

        # 检查请求是否成功
        if response.status_code == 200:
            # 获取图片内容
            image_data = response.content

            file_name = os.path.join(get_project_path(), 'other')

            # 指定保存的文件名和路径
            filename = file_name + "\\" + 'yzm.jpg'  # 可以根据需要修改文件名和扩展名

            # 使用二进制写入模式保存图片
            with open(filename, 'wb') as file:
                file.write(image_data)

            # 识别验证码
            ocr = ddddocr.DdddOcr(beta=True, show_ad=False)

            with open(filename, 'rb') as f:
                image = f.read()

            res = ocr.classification(image)
            print("验证码识别结果：{}".format(res))
            return res
        else:
            print('请求失败')
            print(response.status_code)
            print(response.text)
    else:
        raise Exception('url地址输入错误')


# def parse_yanzheng(path):
#     # 识别验证码
#     ocr = ddddocr.DdddOcr(beta=True, show_ad=False)
#     with open(path, 'rb') as f:
#         image = f.read()
#
#     res = ocr.classification(image)
#     print("验证码识别结果：{}".format(res))
#     return res


if __name__ == '__main__':
    print(parse_yanzheng('url-formal'))

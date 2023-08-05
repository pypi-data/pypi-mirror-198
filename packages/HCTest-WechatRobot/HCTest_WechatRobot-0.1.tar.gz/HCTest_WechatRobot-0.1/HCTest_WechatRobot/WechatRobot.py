# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：WechatRobot.py

import requests
import json
import base64
import hashlib


class WechatRobot:
    API_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook"

    def __init__(self, access_token):
        self.webhook_url = self.API_URL + "/send?key=" + access_token

    def send_text(self, content, mentioned_list=None, mentioned_mobile_list=None):
        data = {
            'msgtype': 'text',
            'text': {
                'content': content,
                'mentioned_list': mentioned_list,
                'mentioned_mobile_list': mentioned_mobile_list
            }
        }
        requests.post(self.webhook_url, data=json.dumps(data))

    def send_markdown(self, content):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }
        requests.post(self.webhook_url, data=json.dumps(data))

    def send_image(self, image_path):
        with open(image_path, 'rb') as f:
            image_data = f.read()
            # 计算图片md5
            md5 = hashlib.md5(image_data).hexdigest()
            # 将图片内容进行加密
            image_content = base64.b64encode(image_data).decode('utf-8')
        data = {
            'msgtype': 'image',
            'image': {
                'base64': image_content,
                'md5': md5
            }
        }
        requests.post(self.webhook_url, data=json.dumps(data))

    def upload_file(self, file_path):
        with open(file_path, 'rb') as f:
            file_data = f.read()

        # 构建上传文件的请求体
        upload_url = self.API_URL + "/upload_media?key=" + self.webhook_url.split("=")[-1] + "&type=file"
        response = requests.post(upload_url, files={f"{file_path.split('/')[-1]}": file_data})
        return response.json()['media_id']

    def send_file(self, file_path, title=None):
        media_id = self.upload_file(file_path)
        data = {
            'msgtype': 'file',
            'file': {
                'media_id': media_id
            }
        }

        # 如果指定了文件标题，则将标题添加到请求体中
        if title:
            data['file']['filename'] = title

        requests.post(self.webhook_url, data=json.dumps(data))


if __name__ == "__main__":
    # WechatRobot 示例代码
    wechat_robot = WechatRobot(access_token="YOUR_ACCESS_TOKEN")
    # 发送文本消息
    content = "这是一条测试文本消息"
    mentioned_list = ["userid1", "userid2"]
    mentioned_mobile_list = ["13800001111", "13800002222"]
    wechat_robot.send_text(content=content, mentioned_list=mentioned_list, mentioned_mobile_list=mentioned_mobile_list)

    content = '''
    # 我是一级标题
    ## 我是二级标题
    ### 我是三级标题
    这是一段普通的文本

    这是一段**加粗**的文本

    这是一个[链接](https://www.example.com)

    这是一个引用
    > 引用的内容

    这是一段<font color="info">绿色</font>文本
    '''

    wechat_robot.send_markdown(content=content)

    # 发送图片消息
    image_path = "/path/to/image.jpg"
    wechat_robot.send_image(image_path=image_path)

    # 发送文件消息
    file_path = "/path/to/file.xx"
    response = wechat_robot.send_file(file_path=file_path)

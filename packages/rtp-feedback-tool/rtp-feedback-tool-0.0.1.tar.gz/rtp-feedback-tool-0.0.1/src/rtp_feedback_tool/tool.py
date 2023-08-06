import numpy as np
from PIL import Image
import base64
from paho.mqtt.publish import single
import os
import io


def text_feedback(content: str) -> None:
    """
    机器人给云端反馈文本数据
    主要是将content发送到本地的mqtt broker, 之后kubeedge帮我们转发到云端的数据收集器
    必须在robot-tasking-platform的operator下发的任务容器中使用才有效(因为下发的任务容器里正确配置了环境变量和转发规则)
    Args:
        content (str): _description_ 要反馈的文本数据内容
    """
    # 获得mqtt话题，只要在这个话题上发送数据，kubeedge就会把数据转发到云端的数据收集器
    mqtt_topic = os.environ.get('TEXT_FEEDBACK_TOPIC')
    if not mqtt_topic:
        mqtt_topic = ""

    # 发送数据
    single(mqtt_topic, payload=content)


def image_feedback(img_rgb8: np.ndarray) -> None:
    """
    机器人给云端反馈图片数据
    主要是将content发送到本地的mqtt broker, 之后kubeedge帮我们转发到云端的数据收集器
    必须在robot-tasking-platform的operator下发的任务容器中使用才有效(因为下发的任务容器里正确配置了环境变量和转发规则)
    Args:
        img_rgb8: 图像,必须是numpy数组,且数据类型为uint8,且shape为(height, width, 3)
    """
    # 获得mqtt话题，只要在这个话题上发送数据，kubeedge就会把数据转发到云端的数据收集器
    mqtt_topic = os.environ.get('IMAGE_FEEDBACK_TOPIC')
    if not mqtt_topic:
        mqtt_topic = ""

    # 将图片从numpy数组形式转换为PIL.Image形式
    img = Image.fromarray(img_rgb8)

    # 将PIL.Image图片转换成JPEG格式的字节数据
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG')
    jpeg_bytes = buffer.getvalue()

    # 对字节数据进行base64编码
    base64_bytes = base64.b64encode(jpeg_bytes)
    base64_str = base64_bytes.decode('utf-8')

    # 添加元信息，使base64_str变成类似于data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAEBAQ.....的格式
    base64_str = "data:image/jpeg;base64,"+base64_str

    # 发送图像数据到本地的mqtt broker，之后由kubeedge转发到云端
    single(mqtt_topic, payload=base64_str)

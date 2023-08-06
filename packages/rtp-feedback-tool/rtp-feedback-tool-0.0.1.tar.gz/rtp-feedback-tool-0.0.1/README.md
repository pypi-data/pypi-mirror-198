# RTP FEEDBACK TOOL(机器人任务下发与状态同步平台)的数据反馈工具

- 功能：处在KubeEdge边缘（Edge）端的机器人给云端（Cloud）反馈数据。
- 只能在obot-tasking-platform的operator下发的任务容器中使用才有效。
- `text_feedback`和`image_feedback`负责将数据发送到边缘端本地的mqtt broker，之后由KubeEdge转发到远端的数据收集器。
- 机器人任务的编写者不需要知道数据收集器具体的url，只需要调用`text_feedback`和`image_feedback`即可。数据转发的路径（route）和规则（rule）是operator在下发任务时就配置好的。

```python
def text_feedback(content: str) -> None:
    """
    机器人给云端反馈文本数据
    主要是将content发送到本地的mqtt broker, 之后kubeedge帮我们转发到云端的数据收集器
    必须在robot-tasking-platform的operator下发的任务容器中使用才有效(因为下发的任务容器里正确配置了环境变量和转发规则)
    Args:
        content (str): _description_ 要反馈的文本数据内容
    """
```

```python
def image_feedback(img_rgb8: np.ndarray) -> None:
    """
    机器人给云端反馈图片数据
    主要是将content发送到本地的mqtt broker, 之后kubeedge帮我们转发到云端的数据收集器
    必须在robot-tasking-platform的operator下发的任务容器中使用才有效(因为下发的任务容器里正确配置了环境变量和转发规则)
    Args:
        img_rgb8: 图像,必须是numpy数组,且数据类型为uint8,且shape为(height, width, 3)
    """
```


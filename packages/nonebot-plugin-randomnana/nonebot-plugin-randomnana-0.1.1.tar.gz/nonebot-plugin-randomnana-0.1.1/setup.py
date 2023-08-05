# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_randomnana']

package_data = \
{'': ['*'], 'nonebot_plugin_randomnana': ['resource/*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.1,<3.0.0', 'nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-randomnana',
    'version': '0.1.1',
    'description': '一款开箱即用的随机抽取神乐七奈表情包图片的插件（适用于Nonebot2 V11）',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot-plugin-randomnana\n\n_✨ 一款开箱即用的随机抽取神乐七奈表情包图片的插件（适用于Nonebot2 V11）✨_\n\n<a href="./LICENSE">\n    <img src="https://camo.githubusercontent.com/6849e28a50157229c6a1426570610ecbe589c68bd7c806f4f7513d7265db8cf2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6e6f6e65706c7567696e2f6e6f6e65626f742d706c7567696e2d706574706574" alt="license">\n</a><img src="https://img.shields.io/badge/nonebot-2.0.0b5+-red.svg" alt="NoneBot">\n<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n\n</div>\n\n## 📖 介绍\n\n一款开箱即用的随机抽取神乐七奈表情包图片的插件（适用于Nonebot2 V11），目前共180张\n\n## 💿 安装\n\n<details>\n<summary>使用PIP安装</summary>\n\n\n    pip install nonebot-plugin-randomnana\n</details>\n\n## 🎉 使用\n### 指令表\n| 指令 | 权限 | 需要@ | 范围 |\n|:-----:|:----:|:----:|:----:|\n| 狗妈 | 所有人 | 否 | 群聊 |\n| 随机狗妈 | 所有人 | 否 | 群聊 |\n### 效果图\n\n<div align="left">\n  <img src="https://s1.vika.cn/space/2023/03/16/c870e999dc4a4472aef90f69f0b7717e?attname=xiaoguo.png"/>\n</div>\n',
    'author': 'NanakoOfficial',
    'author_email': 'demo0929@vip.qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NanakoOfficial/nonebot_plugin_randomnana',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

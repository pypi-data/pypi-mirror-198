# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_ai_interviewer']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.4,<4.0.0',
 'nonebot-adapter-onebot>=2.2.1,<3.0.0',
 'nonebot2>=2.0.0rc3,<3.0.0',
 'openai>=0.27.1,<0.28.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ai-interviewer',
    'version': '0.1.0',
    'description': 'A ai-interviewer based on chatgpt',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot-plugin-ai-interviewer\n</div>\n\n## 介绍\n- 本插件基于OpenAI的API开发，在nonebot框架下实现一个聊天式的可自定义面试职位的AI辅助面试官。\n- 本插件具有用户识别功能\n\n![](demo.jpg)\n## 安装\n\n* 手动安装\n  ```\n  git clone https://github.com/Alpaca4610/nonebot-plugin-ai-interviewer.git\n  ```\n\n  下载完成后在bot项目的pyproject.toml文件手动添加插件：\n\n  ```\n  plugin_dirs = ["xxxxxx","xxxxxx",......,"下载完成的插件路径/nonebot-plugin-ai-interviewer"]\n  ```\n* 使用 pip\n  ```\n  pip install nonebot-plugin-ai-interviewer\n  ```\n\n## 配置文件\n\n在Bot根目录下的.env文件中追加如下内容：\n\n```\nOPENAI_API_KEY = key\n```\n\n可选内容：\n```\nOPENAI_HTTP_PROXY = "http://127.0.0.1:8001"    # 中国大陆/香港IP调用API请使用代理访问api,否则有几率会被封禁\nOPENAI_MODEL_NAME = True   # AI面试官使用的模型名称\n```\n\n\n## 使用方法\n\n- 初始化AI面试官：（注意，命令中的逗号为中文逗号）\n```\ninterviewer 公司：XXXX 职位：XXXXX\n```\n- 回答面试官问题\n```\ninterviewer 你的回答\n```\n- 停止面试，开始下一轮面试需要重新初始化\n```\nstop\n```\n',
    'author': 'Alpaca',
    'author_email': 'alpaca@bupt.edu.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

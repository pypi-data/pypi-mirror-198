# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['teenstudy',
 'teenstudy.models',
 'teenstudy.utils',
 'teenstudy.web',
 'teenstudy.web.api',
 'teenstudy.web.pages',
 'teenstudy.web.utils']

package_data = \
{'': ['*'], 'teenstudy': ['resource/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'Pillow>=9.4.0,<10.0.0',
 'amis-python>=1.0.6,<2.0.0',
 'anti-useragent>=1.0.10,<2.0.0',
 'beautifulsoup4>=4.11.2,<5.0.0',
 'bs4>=0.0.1,<0.0.2',
 'fastapi>=0.90.0,<0.91.0',
 'httpx>=0.23.3,<0.24.0',
 'lxml>=4.9.2,<5.0.0',
 'nonebot-adapter-onebot>=2.2.1,<3.0.0',
 'nonebot-plugin-apscheduler>=0.2.0,<0.3.0',
 'nonebot2>=2.0.0rc2,<3.0.0',
 'python-jose>=3.3.0,<4.0.0',
 'qrcode>=7.4.2,<8.0.0',
 'tortoise-orm>=0.19.3,<0.20.0',
 'ujson>=5.7.0,<6.0.0',
 'uvicorn>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'teenstudy',
    'version': '0.1.4',
    'description': '基于nonebot2异步框架的青年大学自动提交插件基于nonebot2的青年大学习自动提交插件，用于自动完成大学习，在后台留下记录，返回完成截图',
    'long_description': '<div align="center">\n    <img src="https://i.328888.xyz/2023/02/28/z23ho.png" alt="TeenStudy.png" border="0" width="500px" height="500px"/>\n    <h1>TeenStudy</h1>\n    <b>基于nonebot2的青年大学习自动提交插件，用于自动完成大学习，在后台留下记录，返回完成截图</b>\n    <br/>\n    <a href="https://github.com/ZM25XC/TeenStudy/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ZM25XC/TeenStudy?style=flat-square"></a>\n    <a href="https://github.com/ZM25XC/TeenStudy/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/ZM25XC/TeenStudy?style=flat-square"></a>\n    <a href="https://github.com/ZM25XC/TeenStudy/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/ZM25XC/TeenStudy?style=flat-square"></a>\n    <a href="https://pypi.python.org/pypi/TeenStudy"><img src="https://img.shields.io/pypi/v/TeenStudy?color=yellow" alt="pypi"></a>\n  \t<a href="https://pypi.python.org/pypi/TeenStudy">\n    <img src="https://img.shields.io/pypi/dm/TeenStudy" alt="pypi download"></a>\n     <a href="https://github.com/ZM25XC/TeenStudy">\n    <img src="https://visitor-badge.glitch.me/badge?page_id=https://github.com/ZM25XC/TeenStudy" alt="Teenstudy"></a>\n\t<a href="https://github.com/ZM25XC/TeenStudy/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ZM25XC/TeenStudy?style=flat-square"></a>\n    <a href="https://jq.qq.com/?_wv=1027&k=NGFEwXyS">\n    <img src="https://img.shields.io/badge/QQ%E7%BE%A4-511173803-orange?style=flat-square" alt="QQ Chat Group">\n  </a>\n  </div>\n\n## 说明\n\n- 本项目为[青年大学习提交](https://github.com/ZM25XC/nonebot_plugin_auto_teenstudy) `Web UI`版\n- 需要抓包的地区，绑定后尽量别进官方公众号，避免token或cookie刷新导致无法提交\n- 本项目需要部署在公网可访问的容器中，并开放端口（nonebot配置的port），否则大部分功能将出现异常\n- 欢迎加入[QQ群](https://jq.qq.com/?_wv=1027&k=NGFEwXyS)，交流讨论。\n- 时间精力有限，目前只维护湖北和江西两个地区，其他地区出问题请提交Issues,我找个时间修，需要增加地区请进群帮忙测试，个别地区没账号无法测试\n- 觉得项目不错，不妨点个stars.\n\n## 支持地区\n\n### 以下地区无需抓包\n\n- 湖北\n- 江西\n\n### 以下地区使用微信扫码进行绑定\n\n- 浙江\n- 上海\n\n### 以下地区需要抓包\n\n- 江苏\n- 安徽\n- 河南\n- 四川\n- 山东\n- 重庆\n\n\n\n##  安装及更新\n\n1. 使用`git clone https://github.com/ZM25XC/TeenStudy.git`指令克隆本仓库或下载压缩包文件\n2. 使用`pip install TeenStudy`来进行安装,使用`pip install TeenStudy -U`进行更新\n\n## 导入插件\n**使用第一种安装方式**\n\n- 将`TeenStudy`放在nb的`plugins`目录下，运行nb机器人即可\n\n- 文件结构如下\n\n    ```py\n    📦 AweSome-Bot\n    ├── 📂 awesome_bot\n    │   └── 📂 plugins\n    |       └── 📂 TeenStudy\n    |           └── 📜 __init__.py\n    ├── 📜 .env.prod\n    ├── 📜 .gitignore\n    ├── 📜 pyproject.toml\n    └── 📜 README.md\n    ```\n\n    \n\n**使用第二种安装方式**\n- 在`pyproject.toml`里的`[tool.nonebot]`中添加`plugins = ["TeenStudy"]`\n\n\n## 机器人配置\n\n- 在nonebot的`.env` 或 `.env.prod`配置文件中设置好超管账号和公网IP\n\n  ```py\n  SUPERUSERS=[""]\n  DXX_IP=""\n  ```\n\n## 使用方式\n\n- 启动nb,等待插件加载数据，加载完毕后登录后台，账号默认为`nonebot配置文件中的超管账号`，密码默认为：`admin`,开放端口（默认为.env中配置的port）\n- 在管理后台的推送列表中添加需要开启大学习使用的群聊\n\n## 功能列表\n|            指令            |                 指令格式                  |                             说明                             |\n| :------------------------: | :---------------------------------------: | :----------------------------------------------------------: |\n|         添加大学习         |     添加大学习`地区`     |     添加大学习湖北 添加大学习     |\n|         我的大学习         |                我的大学习                 |                         查询个人信息                         |\n|         提交大学习         |                提交大学习 戳一戳Bot                 |                      提交最新一期大学习                      |\n|           大学习           |            大学习答案、大学习、答案截图             |                  获取最新一期青年大学习答案                  |\n|          完成截图          |   完成截图、大学习截图、大学习完成截图    |          获取最新一期青年大学习完成截图（带状态栏）          |\n|          完成大学习          |   完成大学习、全员大学习    |        团支书可用，需要成员填写团支书ID，填写后团支书可发指令提交大学习          |\n|          重置配置          |   重置配置、刷新配置    |         超管可用，刷新Web UI默认配置          |\n|          重置密码          |   重置密码    |          重置登录Web UI的密码为用户ID          |\n\n\n## ToDo\n\n\n- [ ] 增加更多地区支持\n- [ ] 优化 Bot\n\n\n## 更新日志\n\n### 2023/03/18\n- 适配河南地区，需要自行抓包\n- 适配四川地区，需要自行抓包\n- 适配山东地区，需要自行抓包\n- 适配重庆地区，需要自行抓包\n- 添加自动获取公网IP功能，别再问如何配置公网IP啦\n- 添加重置密码功能，指令`重置密码`\n- 添加重置配置功能，指令`重置配置`，`刷新配置`\n- 添加完成大学习功能，团支书可一次性提交全班的大学习，指令`完成大学习`，`全员大学习`\n- 管理后台开放添加用户权限（浙江，上海地区无法添加）\n- 优化用户信息页\n- 优化登录界面提示\n- 将添加链接，登录链接转化成二维码，减少公网IP暴露，没啥用，样式好看一些\n- 修复Ubuntu系统导入资源失败BUG\n\n\n### 2023/03/05\n\n- 适配浙江地区，使用微信扫码进行绑定\n- 适配上海地区，使用微信扫码进行绑定\n- 适配江苏地区，需要自行抓包\n- 适配安徽地区，需要自行抓包\n\n\n### 2023/03/01\n\n- 将代码上传至pypi，可使用`pip install TeenStudy`指令安装本插件\n- 上传基础代码\n- 适配湖北地区，无需抓包，安装即用\n- 适配江西地区，无需抓包，安装即用',
    'author': 'ZM25XC',
    'author_email': 'xingling25@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ZM25XC/TeenStudy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

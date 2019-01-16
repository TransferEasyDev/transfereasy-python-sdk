
![TransferEasy](https://s.transfereasy.com/logo/logo-2-black.png)
<br>
![Travis](https://api.travis-ci.org/nukeop/nuclear.svg?branch=master)
# 汇通天下, 无处不达

* [官方网站](https://www.transfereasy.com)
* [注册体验](https://business.transfereasy.com/Home/register)
* [商务合作](https://www.transfereasy.com/home/merchant)


## 结构

```$xslt
├── config      # 配置文件
├── examples    # DEMO
├── kernel      # API
└── test        # 测试用例

```

## 示例

```
/**
 * 初始化环境
 */

$ cd transfereasy-python-sdk
$ virtualenv ENV
$ source ./ENV/bin/active
$ (ENV) pip install -r requirements.txt

```

```
/**
 * 配置文件
 * 
 * └── config
 *     └── __init__.py
 */

# 在 __init__.py 中控制生产和测试的配置文件开关
from config.test import *  # 沙盒环境
# from config.prod import *  # 生产环境
```

```
/**
 * 配置文件
 *
 * └── config
 *     ├── prod.py*
 *     └── test.py
 */
SECRET = ''         # 登录transfereasy后台进入设置页面查看
ACCOUNT_NO = ''     # 登录transfereasy后台进入设置页面查看
TE_HOST = 'https://stable-api.transfereasy.com/{url}'
```

```python
# -*- coding: utf-8 -*-

# ''' Demo: 查询汇率'''

if __name__ == '__main__':
    from kernel.api.rate import Rate

    # 1. 新建对象
    rate = Rate()

    # 2. 准备参数
    param = {
        'sell_currency': 'USD',
        'buy_currency': 'CNY',
    }

    # 3. 执行
    rate.get_rate(param)



```

## 依赖

* Schemer==0.2.11
* requests==2.18.4
* Flask==1.0.2
* nose==1.3.7
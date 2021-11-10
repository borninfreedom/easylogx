## 使用介绍

我们在写程序的时候，一个功能是需要经常用到的—— log。我们尽量避免使用 print 来调试我们的程序，使用 log 的好处非常多，一个是可以直接通过控制 log 的等级来关掉低等级的 log，这样减少了很多发布的时候删除 print 的工作，同时又能按照log的等级来开关不同的log。

另外一点，相比 print，我们有些场景下，需要调试很多的输出，而且希望看到他们之间的联系，这样在 console 中输出就会显得特别不方便，我们希望将调试的内容输出到文件中。使用 log 来控制调试内容到文件中也是非常方便的，不需要我们自己来写文件的处理工作，我们只需要给 log 添加一个 fileHandler 就可以。

虽然相比 print，log有很多的好处，但是log的初始化和Handler的添加也是需要写几行代码的，最少的情况，也是一个工程中有一个log.py，其他文件通过导入这个文件来使用 log，最差的情况是每个文件都有一堆 log 的初始化代码，所以将这些冗余的工作去掉是很必要的，这也是这个 python 包的制作初衷。

现在只需要在你的 python 环境中，执行

```bash
pip install -U easylogx
```

就把这个 python 包安装成功了，那么以后在自己的工程中，只需要输入

```python
from easylogx import Easylogx

logger = Easylogx() #默认log的名字是__name__,默认log等级是DEBUG
logger.debug('test')
```

就可以实现 console 的 log 调试功能，如果想更进一步，可以给 logger 输入自己指定的名字和 log 的等级

```python
from easylogx import Easylogx, DEBUG, ERROR, INFO

logger = Easylogx('test_log',INFO)
logger.info('info_test')
logger.debug('debug_test')
```

如果想把调试信息同时输出到文件里面，只需要添加一个 fileHandler 就可以了。

```python
from easylogx import Easylogx

logger = Easylogx()
logger.info('info_test')
logger.debug('debug_test')

logger.add_filehandler()  # 默认文件名字是 default.log，默认写入方式是每次执行清空文件再写入
logger.debug('file_test')
```

这时候会自动生成一个 default.log 文件，存储我们的调试信息，我们也可以指定文件的名字和写入的方式，比如每次追加或者每次执行清空文件后再写入。

```python
from easylogx import Easylogx

logger = Easylogx()
logger.info('info_test')
logger.debug('debug_test')

logger.add_filehandler('file_test.log','a')  # 'a'代表每次执行不清空原文件的内容，直接添加新的信息
logger.debug('file_test')
```



## 安装方式

```bash
pip install -U easylogx
```

## 发布到pypi的指令

如果想把自己写的程序发布到pypi，让用户可以直接通过pip install安装来使用，可以参考下面的博客：

发布方法是参考的这个：[发布代码到 PyPI | Python技术 (justdopython.com)](https://www.justdopython.com/2020/05/13/Python-pip/)，

一些问题的处理参考的这个https://stackoverflow.com/questions/52016336/how-to-upload-new-versions-of-project-to-pypi-with-twine

用到的一些指令是：

```bash
pip install setuptools wheel twine
python setup.py bdist_wheel
twine upload dist/*
```



## 获取源码

[borninfreedom/easylogx: 简化了python logging的使用和冗余代码量 (github.com)](https://github.com/borninfreedom/easylogx)
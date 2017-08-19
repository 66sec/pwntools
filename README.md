# pwntools - CTF toolkit
![pwntools logo](https://github.com/Gallopsled/pwntools/blob/stable/docs/source/logo.png?raw=true)

[![Docs](https://readthedocs.org/projects/pwntools/badge/?version=stable)](https://docs.pwntools.com/)
[![PyPI](https://img.shields.io/badge/pypi-v3.8.0-green.svg?style=flat)](https://pypi.python.org/pypi/pwntools/)
[![Travis](https://travis-ci.org/Gallopsled/pwntools.svg)](https://travis-ci.org/Gallopsled/pwntools)
[![Coveralls](https://img.shields.io/coveralls/Gallopsled/pwntools/dev.svg)](https://coveralls.io/github/Gallopsled/pwntools?branch=dev)
[![Twitter](https://img.shields.io/badge/twitter-pwntools-4099FF.svg?style=flat)](https://twitter.com/pwntools)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

Pwntools 是一个用python写的CTF框架和开发漏洞利用的库， 它设计之初就是帮助我们快速简便的开发利用漏洞。

```python
from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('exploitme.example.com', 31337)
# EXPLOIT CODE GOES HERE
r.send(asm(shellcraft.sh()))
r.interactive()
```

# 开始试试吧!

You can now do a live demo of Pwntools, [right in your browser](https://demo.pwntools.com).

# 文档

你可以在这里查看文档 [docs.pwntools.com](https://docs.pwntools.com/)

我们提供了一些CTF题目来帮助你入门。[write-ups repository](https://github.com/Gallopsled/pwntools-write-ups).

# 安装

Pwntools 对64位的Ubuntu支持最好 (12.04, 14.04, and 16.04)，大部分功能能在其他系统上正常运行 (Debian, Arch, FreeBSD, OSX, etc.)，当然Python库需要Python27解析器支持。

pwntools大部分功能函数是独立的。  你可以按一下方式快速入手：

```sh
apt-get update
apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
pip install --upgrade pip
pip install --upgrade pwntools
```

当然，也有一些特性不依赖Python(assembling/disassembling foreign architectures)。想了解更多，查看 [完整安装指南](https://docs.pwntools.com/en/stable/install.html).


# 贡献者

查阅 [CONTRIBUTING.md](CONTRIBUTING.md)

# 联系
If you have any questions not worthy of a [bug report](https://github.com/Gallopsled/pwntools/issues), feel free to ping us
at [`#pwntools` on Freenode](irc://irc.freenode.net/pwntools) and ask away.
Click [here](https://kiwiirc.com/client/irc.freenode.net/pwntools) to connect.
There is also a [mailing list](https://groups.google.com/forum/#!forum/pwntools-users) for higher latency discussion.

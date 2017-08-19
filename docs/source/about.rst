关于 pwntools
========================

你可以用他来编写exploits，或者作为你其他软件项目的一部分，这取决你怎么使用他。

以前pwntools被当成编写exploits的通用范式。在以前的版本中通过``from pwn import *`` 
就可以导入一系列功能库。


在编写2.0版本的pwntools的时候，我们考虑了两个对立的目标：


* 我们想要一个很Python范的模块结构，让其他人容易理解代码结构以致能快速上手。
* 我们也想他能更加便捷，能像终端编辑一样便捷。

为此，我们决定分成两个不同的模块。:mod:`pwnlib`是我们python规范化模块, 而:mod:`pwn` 
主要服务于我们的CTF选手。

:mod:`pwn` --- CTF选手的工具
-----------------------------------------

.. module:: pwn

像前面说的那样，我们这个模块有更多默认的效果，这是我们设计这个模块的初衷。
这个模块主要完成一下事项：
* 从顶层模块:mod:`pwnlib`导入所有函数集。这意味着无论你用
  ``import pwn`` 或者 ``from pwn import *``，你都可以导入所有你想要的模块。
* 调用 :函数:`pwnlib.term.init` to put your terminal in raw mode
  and implements functionality to make it appear like it isn't.
* Setting the :data:`pwnlib.context.log_level` to `"info"`.
* Tries to parse some of the values in :data:`sys.argv` and every
  value it succeeds in parsing it removes.

:mod:`pwnlib` --- 规范化Python库
---------------------------------------

.. module:: pwnlib

这个模块是我规范的Python代码。 我们不认为导入:模块:`pwnlib` 或者是其他认识子模块
要有附加的效果。

你导入什么就只能使用什么。 比如你简单的用``import
pwnlib.util``是不会导入`pwnlib.util.packing`模块的。

尽管有一些细微的模块 (such as :mod:`pwnlib.shellcraft`), 不太符合我们简单规范的要求,但是他们
还是能没有附加导入效果而被使用。
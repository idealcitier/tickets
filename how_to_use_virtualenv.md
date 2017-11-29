> virualenv是Python开发的一个十分有用的利器，可以提供一个管理多个不同版本Python开发的工具。

## virtualenv的安装

```shell
pip install virtualenv
```
## 创建指定版本的虚拟环境

```shell
virtualenv -p [Python版本的的地址] [定义一个环境的名字]

```
eg.
```shell
virtualenv -p /usr/bin/python3 py3env
```
上面的代码就创建了一个Python3的开发环境,同时生成一个py3env的文件夹，用于保存相应的配置，这里就不作过多的介绍。

## 激活开发环境

开发环境安装完成以后，在愉快的玩耍前，需要对开发环境进行激活。
这里仍以上面的栗子为例。
```shell
source [path]/py3env/bin/activate
```
这样就激活了开发的环境，可以愉快的玩耍了。

## 退出模拟的环境

在使用完成以后，可以对虚拟环境退出。
```shell
deactivate
```
de + activate = 这样就好记了。


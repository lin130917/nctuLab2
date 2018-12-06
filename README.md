# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

1. Change the path to ./src/ .
```
$ cd src
```
2. Execute the program.
```
$ ./topology.py
```
3. Use the following iPerf commands to measure the topology.
```
mininet> h2 iperf -s -u -i 1 > ./out/result &
mininet> h6 iperf -c 10.0.0.2 -u -i 1
```
![](/src/Capture.PNG)

---
## Description

### Mininet API in Python

`Mininet`: Network emulation with hosts spawned in network namespaces

`Topo`: Data center network representation for structured multi-trees

`TCLink`: Link with symmetric TC interfaces configured via opts

`dumpNodeConnections`: dumps connections to/from a set of nodes.

`setLogLevel`: set Mininet's default output level.

`CLI`: Simple command-line interface to talk to nodes

### iPerf Commands

```
mininet> h2 iperf -s -u -i 1 > ./out/result &
mininet> h6 iperf -c 10.0.0.2 -u -i 1
```
The above commands will dump the result of iPerf’s measurement into the file ./src/out/result .

| Command line option | Description |
| ------------------- | ----------- |
| -**s**, --server | Run iPerf in server mode. (This will only allow one iperf connection at a time) |
| -**u**, --udp | Use UDP rather than TCP. |
| -**i**, --interval ***n*** | Sets the interval time in seconds between periodic bandwidth, jitter, and loss reports. If non-zero, a report is made every ***interval*** seconds of the bandwidth since the last report. If zero, no periodic reports are printed. Default is zero. |
| -**c**, --client ***host*** | Run iPerf in client mode, connecting to an iPerf server running on ***host***. |

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**


2. **Example of Mininet**


3. **Topology Generator**


4. **Measurement**

---
## References

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

* [林詩哲](https://github.com/lin130917)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3

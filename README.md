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

1. Execute the program.
   ```
   # Change the directory into /Network_Topology/src/
   $ cd /root/Network_Topology/src/
   # Change to the executable mode of topology.py
   $ sudo chmod +x topology.py
   # Run the code (topology.py)
   $ sudo ./topology.py
   ```
2. Use the following iPerf commands to measure the topology.
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
The above commands will dump the result of iPerf’s measurement into the file /Network_Topology/src/out/result .

| Command line option | Description |
| ------------------- | ----------- |
| -**s**, --server | Run iPerf in server mode. (This will only allow one iperf connection at a time) |
| -**u**, --udp | Use UDP rather than TCP. |
| -**i**, --interval ***n*** | Sets the interval time in seconds between periodic bandwidth, jitter, and loss reports. If non-zero, a report is made every ***interval*** seconds of the bandwidth since the last report. If zero, no periodic reports are printed. Default is zero. |
| -**c**, --client ***host*** | Run iPerf in client mode, connecting to an iPerf server running on ***host***. |

### Tasks

1. **Environment Setup**
   1. Join this lab on GitHub Classroom
      - Click the following link to join this lab
         - https://classroom.github.com/a/K8gaizQG
      - Check my repository
         - https://github.com/nctucn/lab2-lin130917
   2. Login to the container using SSH
      ```
      # Open the terminal to connect to the container
      $ ssh root@140.113.195.69 -p 16203
      Password: cn2018
      ```
   3. Clone the GitHub repository
      ```
      $ git clone https://github.com/nctucn/lab2-lin130917.git Network_Topology
      ```
   4. Run Mininet for testing
      ```
      # Start the service of Open vSwitch
      $ sudo service openvswitch-switch start
      # Run Mininet for testing
      $ sudo mn
      ```

2. **Example of Mininet**
   - Run the example code
      ```
      # Change the directory into /Network_Topology/src/
      $ cd /root/Network_Topology/src/
      # Change to the executable mode of example.py
      $ sudo chmod +x example.py
      # Run example code (example.py)
      $ sudo ./example.py
      ```
   - Troubleshooting
      ```
      # If Mininet crashes for some reason, clean it up!
      $ sudo mn -c
      ```

3. **Topology Generator**
   1. View the topology I should generate
      - 0616203 % 3 = 0
      - /Network_Topology/src/topo/topo0.png
   2. Generate the topology via Mininet
      - Write a Python program named topology.py according to topo0.png and put it at the same place with example.py
      - Other requirements
         - Dump every hosts’ connections in the program
            ```
            from mininet.util import dumpNodeConnections
            # Dump every hosts' and switches' connections
            dumpNodeConnections(net.hosts)
            dumpNodeConnections(net.switches)
            ```
         - Enter in the Mininet’s CLI mode in the program
            ```
            from mininet.cli import CLI
            # Add the following code and do NOT use net.stop()
            CLI(net)
            ```
      - Troubleshooting
         ```
         # If Mininet crashes for some reason, clean it up!
         $ sudo mn -c
         ```

4. **Measurement**
   - Use the following iPerf commands to measure the topology.
      ```
      mininet> h2 iperf -s -u -i 1 > ./out/result &
      mininet> h6 iperf -c 10.0.0.2 -u -i 1
      ```
   - The rate of packet loss is an approximate value (21% ~ 26%)

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

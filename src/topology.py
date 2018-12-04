#!/usr/bin/python                                                                            
                                                                                             
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

'''
A network topology which has 9 switches anh 6 hosts.
'''
class MyTopo(Topo):
    def build(self):
        # Add switches to a topology
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        # Add hosts to a topology
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        # Add links to a topology
        self.addLink(s7, s9, bw = 40, delay = '5ms', loss = 2)
        self.addLink(s8, s9, bw = 50, delay = '4ms', loss = 3)
        self.addLink(s1, s7, bw = 23, delay = '1ms', loss = 8)
        self.addLink(s2, s7, bw = 18, delay = '2ms', loss = 9)
        self.addLink(s3, s7, bw = 15, delay = '3ms', loss = 5)
        self.addLink(s4, s8, bw = 19, delay = '0.08ms', loss = 7)
        self.addLink(s5, s8, bw = 30, delay = '0.095ms', loss = 2)
        self.addLink(s6, s8, bw = 20, delay = '0.06ms', loss = 6)
        self.addLink(h1, s1, bw = 10, delay = '0.05ms', loss = 12)
        self.addLink(h2, s2, bw = 5, delay = '2ms', loss = 3)
        self.addLink(h3, s3, bw = 7, delay = '0.063ms', loss = 9)
        self.addLink(h4, s4, bw = 12, delay = '0.04ms', loss = 14)
        self.addLink(h5, s5, bw = 15, delay = '0.03ms', loss = 18)
        self.addLink(h6, s6, bw = 3, delay = '5ms', loss = 2)

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create a topology with 6 hosts and 9 switches
    topo = MyTopo()
    # Create a network
    net = Mininet(topo = topo, link = TCLink)
    # Start a network
    net.start()
    # Dump every hosts' and switches' connections
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)
    # Enter in the Mininet's CLI mode
    CLI(net)

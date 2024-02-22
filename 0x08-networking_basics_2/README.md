**0x08-networking_basics_2**

**localhost/127.0.0.1:**

- **Definition:** A special name and IP address (127.0.0.1) that refer to the **local machine itself**. It's used to access services or resources running on your own computer without going through the network.
- **Usage:**
    - Testing web servers by connecting to `http://localhost:80` (default port).
    - Running local development environments.
    - Communicating with local databases or other services.
- **Importance:** Helps isolate and test components without relying on external resources.

**0.0.0.0:**

- **Definition:** A wildcard IP address that usually means **"all IP addresses on this machine"**. It can represent any of the machine's network interfaces.
- **Usage:**
    - In server configurations, it tells the server to listen on all available interfaces for incoming connections.
    - Can be used in routing rules to match any source or destination address.
- **Caution:** Use carefully in security-sensitive configurations, as it makes the service accessible from any network interface.

**`/etc/hosts`:**

- **Definition:** A system file that maps hostnames to IP addresses, providing an alternative to DNS (Domain Name System).
- **Location:** This file typically resides in the `/etc` directory on Linux/Unix systems and varies on Windows.
- **Entries:** Lines with a hostname followed by one or more space-separated IP addresses.
- **Precedence:** Entries in `/etc/hosts` take precedence over DNS for name resolution, allowing overrides for testing or local development.
- **Example:**

```
127.0.0.1 localhost
::1 localhost
192.168.1.100 my-local-server
```

**Displaying Active Network Interfaces:**

- **Linux/macOS:**
    - `ifconfig` (older) or `ip addr` (newer) commands list network interfaces and their details.
    - Example:

```
$ ifconfig
eth0 Link encap:Ethernet HWaddr 00:15:5E:00:00:00
    inet addr:192.168.1.100 Bcast:192.168.1.255 Mask:255.255.255.0
    inet6 addr: fe80::215:5eff:fe00:e0c0/64 Scope:Link
    UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1

lo        Link encap:Loopback  HWaddr 00:00:00:00:00:00
    inet addr:127.0.0.1 Mask:255.0.0.0
    inet6 addr: ::1/128 Scope:Host
    UP LOOPBACK RUNNING MTU:65536 Metric:1
    RX packets:2614 errors:0 dropped:0 overruns:0 frame:0
    TX packets:2614 errors:0 dropped:0 overruns:0 frame:0
```

- **Windows:**
    - `ipconfig` command in Command Prompt lists network interfaces.
    - Example:

```
Ethernet adapter Ethernet:
   Connection-specific DNS Suffix .
   Link-local IPv6 Address ...
   IPv4 Address. . . . . . . . . : 192.168.1.100
   Subnet Mask . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . : 192.168.1.1
```
## 0x09. Web Infrastructure Design

This document provides an overview of essential concepts in web infrastructure design, helping you understand the building blocks of a robust and reliable web application.

**Network Basics:**

* **The internet:** A vast network of interconnected computers and devices that communicate using standardized protocols.
* **IP address:** A unique identifier assigned to each device on the internet, allowing them to locate and communicate with each other.
* **Network protocols:** Rules and guidelines that govern communication between devices on a network, like TCP/IP (Transmission Control Protocol/Internet Protocol).

**Server:**

A dedicated computer responsible for storing, processing, and delivering data and resources to clients (e.g., web browsers) upon request.

**Web Server:**

A specialized server software that processes HTTP requests from web browsers and delivers the requested web pages or resources. Popular web servers include Apache, Nginx, and IIS.

**DNS (Domain Name System):**

A distributed database that translates human-readable domain names (e.g., [www.example.com](https://www.example.com)) into machine-readable IP addresses, enabling users to access websites easily.

**Load Balancer:**

Distributes incoming traffic across multiple web servers, ensuring efficient resource utilization, improved scalability, and high availability.

**Monitoring:**

The continuous process of observing and analyzing the health and performance of various system components (servers, networks, applications) to identify and address potential issues proactively.

**Database:**

A structured collection of data organized for efficient storage, retrieval, and management. Popular database types include relational databases (e.g., MySQL, PostgreSQL) and NoSQL databases (e.g., MongoDB).

**Web Server vs. App Server:**

* **Web server:** Serves static content like HTML, CSS, and images, and interacts directly with web browsers.
* **App Server:** Executes dynamic application logic, interacts with databases, and generates dynamic content for web pages. In some cases, a single server can handle both tasks.

**DNS Record Types:**

Different types of DNS records map domain names to various resources:

* **A record:** Maps a domain name to an IP address (e.g., [www.example.com](https://www.example.com) -> 192.168.1.100).
* **CNAME record:** Aliases one domain name to another.
* **MX record:** Specifies mail servers for a domain.

**Single Point of Failure (SPOF):**

A single component whose failure can bring down the entire system. Redundancy is crucial to eliminate or mitigate SPOFs.

**Avoiding Downtime During Deployments:**

* **Blue-green deployments:** Deploy new code to a separate environment, switch traffic only after successful testing, and roll back if necessary.
* **Rolling deployments:** Gradually update servers with new code, minimizing downtime.
* **Canary deployments:** Deploy new code to a small subset of users to test and monitor before wider rollout.

**High Availability Cluster (Active-Active/Active-Passive):**

A group of servers working together to provide continuous service even if one or more servers fail:

* **Active-active:** All servers handle traffic simultaneously, sharing the load and ensuring high availability.
* **Active-passive:** One server is active, serving traffic, while others are passive backups, ready to take over if the primary fails.

**HTTPS (Hypertext Transfer Protocol Secure):**

Encrypts communication between web browsers and servers, protecting data from eavesdropping and tampering.

**Firewall:**

A security system that monitors incoming and outgoing network traffic, filtering and blocking malicious traffic to protect your system from unauthorized access.

By understanding these core concepts, you can lay the foundation for designing and deploying robust, scalable, and secure web infrastructure.
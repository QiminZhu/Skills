# Lecture 9 — priority review

Confirm or change each suggested priority. Nothing is generated for the final bank until every row is confirmed.

| Unit | Topic | Kind | Suggested | Statement | Slides |
| --- | --- | --- | --- | --- | --- |
| U01 | Role of the data link layer | concept | **core** | Explain that a link joins two adjacent nodes and that links on one path can be of different types (wired, wireless). | 4, 5, 44 |
| U02 | Role of the data link layer | procedure | **core** | Trace how a datagram is put in a new frame for each link: the sender frames it, each router removes the frame and builds a new one for the next link. | 6, 17, 18, 44 |
| U03 | Role of the data link layer | distinction | **core** | Distinguish logical end-to-end communication of upper layers from hop-by-hop delivery at the data link and physical layers. | 17 |
| U04 | Problems the data link layer solves | concept | **supporting** | Identify the physical-layer limits (no error repair, inefficient FDM/TDM sharing, no rate adaptation) that the data link layer addresses. | 7 |
| U05 | Problems the data link layer solves | distinction | **core** | Distinguish a single-bit error from a burst error and measure burst length from the first to the last corrupted bit. | 8 |
| U06 | Problems the data link layer solves | distinction | **supporting** | Distinguish error detection from error correction (FEC done by the receiver). | 9 |
| U07 | Problems the data link layer solves | concept | **core** | Explain that flow control stops a sender from overwhelming a receiver, and that frames arriving at a full buffer are dropped. | 10, 11 |
| U08 | Problems the data link layer solves | concept | **core** | Explain why media access control is needed when stations share a medium without FDM or TDM, and that collisions can occur. | 12, 14 |
| U09 | Problems the data link layer solves | distinction | **supporting** | Distinguish dedicated links (full-duplex switch, star) from shared links (bus, wireless). | 13 |
| U10 | Sublayers and framing | fact | **supporting** | Assign data link functions to LLC (upper-layer multiplexing) and MAC (framing, addressing, FCS, medium access); error recovery and flow control are optional. | 15, 19 |
| U11 | Sublayers and framing | concept | **core** | Explain framing: the header carries control information and link addresses; the trailer carries the FCS for error detection. | 16, 18 |
| U12 | Sublayers and framing | fact | **detail** | State that Wireshark normally hides the Ethernet preamble, SFD and FCS. | 18 |
| U13 | Sublayers and framing | fact | **detail** | Match example link types to protocols and architectures (Ethernet LLC/SNAP + MAC; PPP and HDLC frame directly). | 19 |
| U14 | HDLC | distinction | **core** | Distinguish the HDLC modes NRM, ARM and ABM by which station may start a transmission. | 20, 21 |
| U15 | HDLC | procedure | **core** | Order the basic HDLC frame fields: Flag, Address, Control, Data, FCS, Flag. | 22, 23 |
| U16 | HDLC | fact | **supporting** | State the HDLC field sizes: Flag 8 bits, Address 8 or more bits, Control 8 or 16 bits, FCS 16 or 32 bits. | 22 |
| U17 | HDLC | concept | **core** | Explain the role of each HDLC field: Flag delimits, Address names the secondary station, Control carries frame type and sequence data, FCS detects errors. | 22 |
| U18 | HDLC | distinction | **core** | Distinguish I-, S- and U-frames by purpose and by the first control-field bits (0, 10, 11). | 23 |
| U19 | HDLC | fact | **supporting** | Recall the S-frame function codes: RR 00, REJ 01, RNR 10, SREJ 11. | 23 |
| U20 | HDLC | concept | **detail** | Relate PPP, Cisco HDLC and LAPB to HDLC-style framing, and contrast ATM fixed 53-byte cells. | 24 |
| U21 | Addressing and casting | fact | **core** | Match the four address types (MAC, IP, port, application-level) to their layer and an example. | 26, 30 |
| U22 | Addressing and casting | concept | **core** | Explain that IP addresses stay the same end to end while link-layer addresses change at every hop. | 27, 52, 53, 54, 55 |
| U23 | Addressing and casting | distinction | **core** | Distinguish unicast, anycast, multicast and broadcast; Ethernet supports unicast, multicast and broadcast, while anycast is normally a network-layer function. | 28, 29 |
| U24 | Addressing and casting | fact | **supporting** | Recognise the broadcast MAC FF:FF:FF:FF:FF:FF and multicast MACs starting 01:00:5E. | 29, 51 |
| U25 | Addressing and casting | procedure | **detail** | Find a device's MAC and IP addresses (ipconfig /all, ip link show, ifconfig -a, device settings). | 31, 32, 33, 34 |
| U26 | DHCP | concept | **core** | Explain that DHCP gives a new host its IP address, subnet mask, gateway and DNS settings, and that it developed from BOOTP. | 35, 37 |
| U27 | DHCP | procedure | **core** | Order the DHCP exchange: Discover, Offer, Request, Ack. | 35, 36, 39, 40, 41, 42 |
| U28 | DHCP | fact | **supporting** | State which DHCP messages the client broadcasts (Discover, Request) and which the server sent unicast in the lecture capture (Offer, Ack). | 29, 36, 40, 42 |
| U29 | DHCP | fact | **supporting** | Read DHCP captures: the client starts from 0.0.0.0 to 255.255.255.255 and uses UDP port 68; the server uses port 67. | 39, 40, 41, 42 |
| U30 | DHCP | procedure | **detail** | Trigger and capture a DHCP exchange (ipconfig /release and /renew; dhclient, nmcli, networkctl). | 39, 43 |
| U31 | Switches and routers | procedure | **core** | Explain how a switch learns which MAC address is on which port and records it in its MAC table. | 45 |
| U32 | Switches and routers | distinction | **core** | Distinguish switches (layer 2, MAC, frames, one broadcast domain, forwards unknown destinations out other ports) from routers (layer 3, IP, packets, between networks, drop unknown destinations). | 47 |
| U33 | Switches and routers | concept | **detail** | Read a routing table entry chosen by metric (EIGRP feasible distance, next hop). | 46 |
| U34 | ARP and RARP | concept | **core** | Explain that ARP finds the link-layer address that matches a known IP address on the local link. | 48 |
| U35 | ARP and RARP | distinction | **core** | Distinguish an ARP request (broadcast, opcode 1, target MAC all zeros) from an ARP reply (unicast, opcode 2). | 49, 50, 56, 57 |
| U36 | ARP and RARP | procedure | **core** | Trace ARP across networks: the sender resolves its gateway, each router resolves the next hop, and the last router resolves the destination host. | 52, 53, 54, 55 |
| U37 | ARP and RARP | procedure | **detail** | View and clear the ARP cache (arp -a, arp -d, netsh interface ip delete arpcache). | 51 |
| U38 | ARP and RARP | concept | **detail** | Explain that RARP lets a host learn its own IP address from a RARP server using its MAC address (legacy). | 58 |
| U39 | Problems the data link layer solves | concept | **supporting** | Read a collision-timing diagram: on a shared medium a frame is vulnerable to collision for 2 × T_fr (one frame time before and after it starts). | 14 |
| U40 | HDLC | distinction | **detail** | Distinguish serial links (one bit at a time, point-to-point, e.g. HDLC) from parallel links (several bits at a time, short distances). | 20 |

import json, hashlib, sys
from collections import Counter

PDF = '/root/qm-run/lecture9.pdf'
FILE = 'ITCS217-Lecture_9-Intro-to_Data-Link-Layer-2026.pdf'
sha = hashlib.sha256(open(PDF, 'rb').read()).hexdigest()

# unitId, topic, kind, priority (suggested), statement, pages, contrasts, misconceptions
U = [
 ('U01','T1','concept','core','Explain that a link joins two adjacent nodes and that links on one path can be of different types (wired, wireless).',[4,5,44],[],['The data link layer delivers data end to end']),
 ('U02','T1','procedure','core','Trace how a datagram is put in a new frame for each link: the sender frames it, each router removes the frame and builds a new one for the next link.',[6,17,18,44],[],['Routers forward the original frame unchanged']),
 ('U03','T1','distinction','core','Distinguish logical end-to-end communication of upper layers from hop-by-hop delivery at the data link and physical layers.',[17],['U01','U02'],['Every layer communicates hop by hop']),
 ('U04','T2','concept','supporting','Identify the physical-layer limits (no error repair, inefficient FDM/TDM sharing, no rate adaptation) that the data link layer addresses.',[7],[],[]),
 ('U05','T2','distinction','core','Distinguish a single-bit error from a burst error and measure burst length from the first to the last corrupted bit.',[8],[],['Burst length counts only the flipped bits']),
 ('U06','T2','distinction','supporting','Distinguish error detection from error correction (FEC done by the receiver).',[9],[],['Detecting an error also fixes it']),
 ('U07','T2','concept','core','Explain that flow control stops a sender from overwhelming a receiver, and that frames arriving at a full buffer are dropped.',[10,11],[],['Flow control fixes bit errors']),
 ('U08','T2','concept','core','Explain why media access control is needed when stations share a medium without FDM or TDM, and that collisions can occur.',[12,14],[],[]),
 ('U09','T2','distinction','supporting','Distinguish dedicated links (full-duplex switch, star) from shared links (bus, wireless).',[13],[],[]),
 ('U10','T3','fact','supporting','Assign data link functions to LLC (upper-layer multiplexing) and MAC (framing, addressing, FCS, medium access); error recovery and flow control are optional.',[15,19],[],[]),
 ('U11','T3','concept','core','Explain framing: the header carries control information and link addresses; the trailer carries the FCS for error detection.',[16,18],[],['The FCS sits in the frame header']),
 ('U12','T3','fact','detail','State that Wireshark normally hides the Ethernet preamble, SFD and FCS.',[18],[],[]),
 ('U13','T3','fact','detail','Match example link types to protocols and architectures (Ethernet LLC/SNAP + MAC; PPP and HDLC frame directly).',[19],[],[]),
 ('U14','T4','distinction','core','Distinguish the HDLC modes NRM, ARM and ABM by which station may start a transmission.',[20,21],[],['In ARM the secondary controls the link']),
 ('U15','T4','procedure','core','Order the basic HDLC frame fields: Flag, Address, Control, Data, FCS, Flag.',[22,23],[],[]),
 ('U16','T4','fact','supporting','State the HDLC field sizes: Flag 8 bits, Address 8 or more bits, Control 8 or 16 bits, FCS 16 or 32 bits.',[22],[],[]),
 ('U17','T4','concept','core','Explain the role of each HDLC field: Flag delimits, Address names the secondary station, Control carries frame type and sequence data, FCS detects errors.',[22],[],['The address field holds the sender address']),
 ('U18','T4','distinction','core','Distinguish I-, S- and U-frames by purpose and by the first control-field bits (0, 10, 11).',[23],[],['S-frames carry user data']),
 ('U19','T4','fact','supporting','Recall the S-frame function codes: RR 00, REJ 01, RNR 10, SREJ 11.',[23],[],[]),
 ('U20','T4','concept','detail','Relate PPP, Cisco HDLC and LAPB to HDLC-style framing, and contrast ATM fixed 53-byte cells.',[24],[],[]),
 ('U21','T5','fact','core','Match the four address types (MAC, IP, port, application-level) to their layer and an example.',[26,30],[],['MAC addresses identify hosts across the Internet']),
 ('U22','T5','concept','core','Explain that IP addresses stay the same end to end while link-layer addresses change at every hop.',[27,52,53,54,55],[],['Link-layer addresses are end to end like IP addresses']),
 ('U23','T5','distinction','core','Distinguish unicast, anycast, multicast and broadcast; Ethernet supports unicast, multicast and broadcast, while anycast is normally a network-layer function.',[28,29],[],['Anycast is an Ethernet address type']),
 ('U24','T5','fact','supporting','Recognise the broadcast MAC FF:FF:FF:FF:FF:FF and multicast MACs starting 01:00:5E.',[29,51],[],[]),
 ('U25','T5','procedure','detail','Find a device\'s MAC and IP addresses (ipconfig /all, ip link show, ifconfig -a, device settings).',[31,32,33,34],[],[]),
 ('U26','T6','concept','core','Explain that DHCP gives a new host its IP address, subnet mask, gateway and DNS settings, and that it developed from BOOTP.',[35,37],[],[]),
 ('U27','T6','procedure','core','Order the DHCP exchange: Discover, Offer, Request, Ack.',[35,36,39,40,41,42],[],['The client sends Request before receiving an Offer']),
 ('U28','T6','fact','supporting','State which DHCP messages the client broadcasts (Discover, Request) and which the server sent unicast in the lecture capture (Offer, Ack).',[29,36,40,42],[],[]),
 ('U29','T6','fact','supporting','Read DHCP captures: the client starts from 0.0.0.0 to 255.255.255.255 and uses UDP port 68; the server uses port 67.',[39,40,41,42],[],[]),
 ('U30','T6','procedure','detail','Trigger and capture a DHCP exchange (ipconfig /release and /renew; dhclient, nmcli, networkctl).',[39,43],[],[]),
 ('U31','T7','procedure','core','Explain how a switch learns which MAC address is on which port and records it in its MAC table.',[45],[],[]),
 ('U32','T7','distinction','core','Distinguish switches (layer 2, MAC, frames, one broadcast domain, forwards unknown destinations out other ports) from routers (layer 3, IP, packets, between networks, drop unknown destinations).',[47],[],['A router floods packets with unknown destinations']),
 ('U33','T7','concept','detail','Read a routing table entry chosen by metric (EIGRP feasible distance, next hop).',[46],[],[]),
 ('U34','T8','concept','core','Explain that ARP finds the link-layer address that matches a known IP address on the local link.',[48],[],['ARP finds an IP address from a MAC address']),
 ('U35','T8','distinction','core','Distinguish an ARP request (broadcast, opcode 1, target MAC all zeros) from an ARP reply (unicast, opcode 2).',[49,50,56,57],[],['The ARP request is sent to the target MAC']),
 ('U36','T8','procedure','core','Trace ARP across networks: the sender resolves its gateway, each router resolves the next hop, and the last router resolves the destination host.',[52,53,54,55],[],['The sender resolves the destination host MAC directly']),
 ('U37','T8','procedure','detail','View and clear the ARP cache (arp -a, arp -d, netsh interface ip delete arpcache).',[51],[],[]),
 ('U38','T8','concept','detail','Explain that RARP lets a host learn its own IP address from a RARP server using its MAC address (legacy).',[58],[],[]),
 ('U39','T2','concept','supporting','Read a collision-timing diagram: on a shared medium a frame is vulnerable to collision for 2 × T_fr (one frame time before and after it starts).',[14],[],['A frame can only collide while it is being sent']),
 ('U40','T4','distinction','detail','Distinguish serial links (one bit at a time, point-to-point, e.g. HDLC) from parallel links (several bits at a time, short distances).',[20],[],[]),
]
TOPICS = {'T1':'Role of the data link layer','T2':'Problems the data link layer solves','T3':'Sublayers and framing','T4':'HDLC','T5':'Addressing and casting','T6':'DHCP','T7':'Switches and routers','T8':'ARP and RARP'}

ADMIN = {1:'Title slide',2:'Quote of the week',3:'Copyright notice',25:'Break and exercise prompt',59:'Exercise prompt'}
EXTERNAL = {38:'Links to an external video and article only; not inspected'}

page_units = {}
for u in U:
    for p in u[5]:
        page_units.setdefault(p, []).append(u[0])

accounting = []
for p in range(1, 60):
    if p in ADMIN:
        accounting.append(dict(file=FILE, page=p, disposition='administrative', reason=ADMIN[p], unitIds=[]))
    elif p in EXTERNAL:
        accounting.append(dict(file=FILE, page=p, disposition='external_resource', reason=EXTERNAL[p], unitIds=[]))
    elif p in page_units:
        accounting.append(dict(file=FILE, page=p, disposition='included', reason='Teaching content', unitIds=page_units[p]))
    else:
        sys.exit(f'page {p} unaccounted')

RFC2131 = dict(title='RFC 2131: Dynamic Host Configuration Protocol, section 4.1', url='https://www.rfc-editor.org/rfc/rfc2131.txt')
RFC903 = dict(title='RFC 903: A Reverse Address Resolution Protocol', url='https://www.rfc-editor.org/rfc/rfc903')
RFC6747 = dict(title='RFC 6747: ARP for ILNPv4', url='https://www.rfc-editor.org/rfc/rfc6747')
CISCO = dict(title='Cisco: How to Verify Cisco Express Forwarding Switching', url='https://www.cisco.com/c/en/us/support/docs/routers/12000-series-routers/47321-ciscoef.html')
issues = [
 dict(sourceRefs=[dict(file=FILE, page=7)], status='unresolved', externalRefs=[],
      finding='The slide lists three issues (error, multiple access, flow control) but says the data link layer solves "these two issues".',
      resolution='Proposed: follow slide 15, which lists flow control as an optional data link function. Internal inconsistency; no outside source needed. Awaiting your OK.'),
 dict(sourceRefs=[dict(file=FILE, page=29), dict(file=FILE, page=36)], status='unresolved', externalRefs=[RFC2131],
      finding='Offer and Ack are labelled unicast. Per RFC 2131 section 4.1, the server broadcasts them when the client sets the BROADCAST bit, and unicasts them when the bit is clear. The lecture capture (slides 40, 42) shows unicast.',
      resolution='Proposed: questions say "in the lecture capture" and never state unicast as a general rule. Awaiting your OK.'),
 dict(sourceRefs=[dict(file=FILE, page=58)], status='unresolved', externalRefs=[RFC903],
      finding='The RARP diagram shows the request sent to the server MAC with an IP header. RFC 903 specifies RARP at the data-link level with its own EtherType, not inside IP, on a broadcast medium where any RARP server may answer.',
      resolution='Proposed: keep U38 as detail and test only its purpose (MAC to IP), not the frame layout. Awaiting your OK.'),
 dict(sourceRefs=[dict(file=FILE, page=47)], status='unresolved', externalRefs=[CISCO],
      finding='The table says a switch "will broadcast" an unknown destination (it floods that frame out its other ports) and that routing is slower because it is software based. Cisco documents distributed CEF, where line cards forward packets using a hardware forwarding plane.',
      resolution='Proposed: test only layer, address type, data unit, broadcast domain and unknown-destination behaviour, worded as "sends it out every other port". Awaiting your OK.'),
 dict(sourceRefs=[dict(file=FILE, page=48)], status='unresolved', externalRefs=[RFC6747],
      finding='The diagram labels ARP as "rfc6747". RFC 6747 is an ARP extension for ILNPv4; base ARP is RFC 826, which the slide also lists beside the diagram.',
      resolution='Proposed: never ask for ARP\'s RFC number; if needed, use RFC 826. Awaiting your OK.'),
]

for a in accounting:
    a['inspection'] = 'image and extracted text'

topics = {}
for u in U:
    topics.setdefault(u[1], []).append(dict(
        unitId=u[0], kind=u[2], statement=u[4], priority=u[3], prioritySource='suggested',
        misconceptions=u[7], contrasts=u[6], sourceRefs=[dict(file=FILE, page=p) for p in u[5]]))

catalog = dict(
    catalogId='ITCS217-L9', status='draft', subject='ITCS217 Data Communications and Networking',
    sourceFiles=[dict(file=FILE, version=sha, pageCount=59)],
    lectures=[dict(lectureId='L9', title='Introduction to Data Link Layer',
        topics=[dict(topicId=t, name=TOPICS[t], units=topics[t]) for t in TOPICS])],
    pageAccounting=accounting, sourceIssues=issues)

json.dump(catalog, open('/root/qm-run/catalog.json', 'w'), indent=2, ensure_ascii=False)

# priority review sheet
rows = ['| Unit | Topic | Kind | Suggested | Statement | Slides |', '| --- | --- | --- | --- | --- | --- |']
for u in U:
    rows.append(f'| {u[0]} | {TOPICS[u[1]]} | {u[2]} | **{u[3]}** | {u[4]} | {", ".join(map(str, u[5]))} |')
open('/root/qm-run/priority-review.md', 'w').write('# Lecture 9 — priority review\n\nConfirm or change each suggested priority. Nothing is generated for the final bank until every row is confirmed.\n\n' + '\n'.join(rows) + '\n')

c = Counter(u[3] for u in U)
print('sha', sha); print('units', len(U), dict(c))
print('dispositions', Counter(a['disposition'] for a in accounting))
for half, rng in (('A', range(1, 25)), ('B', range(26, 59))):
    core = [u[0] for u in U if u[3] == 'core' and min(u[5]) in rng]
    print(half, 'core', len(core), core)

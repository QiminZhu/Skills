import json
F = 'ITCS217-Lecture_9-Intro-to_Data-Link-Layer-2026.pdf'
def refs(*p): return [dict(file=F, page=x) for x in p]
def base(i, unit, topic, role, kind, diff, level, prompt, pages):
    return dict(id=f'L9-Q{i:02d}', subject='ITCS217', topic=topic, unitId=unit, lectureId='L9',
                cognitiveRole=role, type=kind, difficulty=diff, cognitiveLevel=level, prompt=prompt,
                sourceRefs=refs(*pages), status='draft', version=1, confidenceCheck=True)

Q = []
q = base(1,'U27','DHCP','recall','ordering','Easy','Remember',
  'A new laptop joins the lecture network and gets its address by DHCP. Put the four DHCP messages in the order they are sent, first to last.',[35,39,40,41,42])
q.update(items=['DHCP Request','DHCP Discover','DHCP Ack','DHCP Offer'], correctOrder=[1,3,0,2],
  stepExplanations=['Discover comes first: the client has no address and looks for any DHCP server.',
                    'Offer: a server proposes an address to the client.',
                    'Request: the client asks to use the offered address.',
                    'Ack: the server confirms, and the client can now use the address.'],
  explanation='Slides 39 to 42 show the same exchange in Wireshark: Discover, Offer, Request, then Ack.')
Q.append(q)

q = base(2,'U35','ARP and RARP','application','two_tier','Medium','Apply',
  'Host A (10.34.10.44) needs to send to host B (10.34.10.80) on the same LAN. A\'s ARP cache has no entry for B.',[49,50,56])
q.update(answerTier=dict(prompt='Which destination MAC address does A put on the frame that carries its ARP request?',
    answers=['FF:FF:FF:FF:FF:FF','00:00:00:00:00:00','B\'s MAC address','The default gateway\'s MAC address'], correct=[0],
    optionExplanations=['Correct: the ARP request frame is a broadcast (slides 49, 56).',
                        'All zeros is the empty target-MAC field inside the ARP message, not the frame destination.',
                        'A cannot address B directly: B\'s MAC is exactly what A is asking for.',
                        'B is on the same LAN, so A resolves B itself; the gateway is only used for other networks.'],
    misconceptions=[None,'Confuses the ARP target-MAC field with the frame destination','Assumes the sender already knows the MAC it is asking for','Thinks ARP always goes through the default gateway']),
  reasonTier=dict(prompt='Why is that the right destination?',
    answers=['A does not know B\'s MAC yet, so every node must hear it','Broadcast frames reach their target faster than unicast','The switch answers ARP requests on behalf of hosts','The target-MAC field is all zeros, so the frame is too'], correct=[0],
    optionExplanations=['Correct: only the node that owns 10.34.10.80 replies, and its reply is unicast (slide 50).',
                        'Speed is not the reason; reach is.',
                        'In the lecture, host B itself sends the ARP reply (slide 57).',
                        'The two fields are separate; the zeros only mark the unknown answer.'],
    misconceptions=[None,'Believes broadcast is a speed optimisation','Thinks switches resolve ARP','Merges the ARP payload with the Ethernet header']),
  explanation='An ARP request is broadcast because the sender does not yet know the receiver\'s link-layer address; the reply comes back unicast.')
Q.append(q)

q = base(3,'U36','ARP and RARP','application','single','Medium','Apply',
  'Alice (network N1) sends data to Bob on a different network, through routers R1 and R2. Alice\'s ARP cache is empty. Whose MAC address does Alice\'s first ARP request ask for?',[52,53,54])
q.update(answers=['R1, Alice\'s default gateway','Bob\'s computer','R2, the router on Bob\'s network','Bob\'s IP address'], correct=[0],
  optionExplanations=['Correct: Alice frames the data for her default gateway R1, so she resolves R1\'s MAC (slide 52).',
                      'Bob is on another network; Alice never needs his MAC. R2 resolves it at the last hop (slide 54).',
                      'R2 is two links away; R1 resolves R2\'s MAC for the middle hop (slide 53).',
                      'Alice already knows Bob\'s IP address; ARP resolves IP to MAC, not the reverse.'],
  misconceptions=[None,'Treats link-layer addresses as end to end','Skips the first hop','Reverses the direction of ARP'],
  explanation='Each sender only resolves the next hop on its own link: Alice resolves R1, R1 resolves R2, and R2 resolves Bob.')
Q.append(q)

q = base(4,'U22','Addressing and casting','application','multiple','Medium','Analyze',
  'A packet goes from Alice to Bob through R1 and R2, as on slides 52 to 55. Select ALL values that are the same on every link of the path.',[27,52,53,54,55])
q.update(answers=['Source IP address','Destination IP address','Source MAC address','Destination MAC address'], correct=[0,1],
  optionExplanations=['Correct: the IP header keeps Alice\'s address (NA) end to end.',
                      'Correct: the IP header keeps Bob\'s address (NB) end to end.',
                      'Each router builds a new frame with its own interface as the source.',
                      'Each frame is addressed to the next hop only (L1, then L3, then LB).'],
  misconceptions=[None,None,'Believes the original sender MAC travels end to end','Believes the frame is addressed to the final host'],
  explanation='IP addresses identify the two end hosts and stay fixed; link-layer addresses identify the two ends of the current link and change at every hop.')
Q.append(q)

q = base(5,'U18','HDLC','recall','matching','Easy','Remember',
  'Match each HDLC frame type to its purpose. Each purpose is used once.',[23])
q.update(leftItems=['Information frame (I-frame)','Supervisory frame (S-frame)','Unnumbered frame (U-frame)'],
  rightItems=['System and link management','Carrying user data','Flow and error control'], reuseRight=False,
  matches=[[0,1],[1,2],[2,0]],
  pairExplanations=['I-frames carry the information (user data).','S-frames carry flow and error control, such as RR and REJ.','U-frames are reserved for system and link management.'],
  explanation='The control field tells the receiver which of the three frame types it has received (slide 23).')
Q.append(q)

q = base(6,'U05','Problems the data link layer solves','application','single','Medium','Apply',
  'In a 16-bit frame, only bits 4, 5, 8 and 11 (counting from 1) are corrupted. How should this error be described?',[8])
q.update(answers=['A burst error of length 8','A burst error of length 4','Four single-bit errors','A burst error of length 16'], correct=[0],
  optionExplanations=['Correct: burst length runs from the first corrupted bit (4) to the last (11), so 11 − 4 + 1 = 8. This matches slide 8.',
                      'Four is the number of flipped bits, not the length of the burst.',
                      'Several corrupted bits close together form one burst error, not separate single-bit errors.',
                      'The burst stops at the last corrupted bit; bits 12 to 16 are unaffected.'],
  misconceptions=[None,'Counts only flipped bits as the burst length','Treats each flipped bit as a separate error','Assumes the whole frame is the burst'],
  explanation='A burst error is measured from the first to the last corrupted bit; bits inside the burst may or may not be flipped.')
Q.append(q)

q = base(7,'U32','Switches and routers','comparison','single','Medium','Analyze',
  'A switch receives a frame for a MAC address that is not in its MAC table. A router receives a packet for a network that is not in its routing table and it has no default route. What does each device do, according to slide 47?',[47])
q.update(answers=['Switch: out every other port. Router: drops it','Switch: drops it. Router: drops it','Switch: out every other port. Router: out every interface','Switch: drops it. Router: out every interface'], correct=[0],
  optionExplanations=['Correct: the switch floods unknown destinations in its broadcast domain; the router discards packets it cannot route.',
                      'A switch does not drop an unknown destination; it floods it.',
                      'A router does not flood; that would spread traffic across separate networks.',
                      'This swaps the two behaviours.'],
  misconceptions=[None,'Thinks switches discard unknown frames','Thinks routers flood like switches','Swaps switch and router behaviour'],
  explanation='Switches work inside one broadcast domain and flood unknown MACs; routers join different networks and drop packets with no route.')
Q.append(q)

q = base(8,'U02','Role of the data link layer','explain','self_explain','Medium','Understand',
  'In 2 to 3 sentences, explain why a router removes the incoming frame and builds a new frame, instead of forwarding the original frame unchanged.',[6,17,18])
q.update(modelAnswer='Each link can be a different type, such as Wi-Fi (802.11) on one side and Ethernet (802.3) on the other, so the next link may need a different frame format. Link-layer addresses only name the two ends of the current link, so the router writes new source and destination MAC addresses for the next hop. The IP packet inside stays the same.',
  checklist=['Says links can be of different types or frame formats','Says link-layer addresses are only valid for one link','Says the IP packet inside is kept unchanged'],
  explanation='Self-graded practice; not scored and not counted as coverage evidence.')
Q.append(q)

q = base(9,'U29','DHCP','recall','fill_blank','Easy','Remember',
  'In the lecture\'s DHCP Discover capture, the client sends from UDP port {{1}} to server port {{2}}.',[39,41])
q.update(blanks=[dict(id='1',kind='number',value=68,absoluteTolerance=0,unit='',rounding='none',explanation='Slide 39: the client source port is 68.'),
                 dict(id='2',kind='number',value=67,absoluteTolerance=0,unit='',rounding='none',explanation='Slide 39: the server destination port is 67.')],
  explanation='DHCP clients use UDP port 68 and servers use port 67, as the Wireshark captures show.')
Q.append(q)

q = base(10,'U14','HDLC','comparison','single','Medium','Understand',
  'Which HDLC mode lets both stations start a transmission as equal peers?',[20,21])
q.update(answers=['Asynchronous Balanced Mode (ABM)','Normal Response Mode (NRM)','Asynchronous Response Mode (ARM)','All three modes'], correct=[0],
  optionExplanations=['Correct: in ABM both combined stations can send commands and responses (slide 21).',
                      'In NRM the secondary only transmits after the primary polls it.',
                      'In ARM the secondary may start a transmission, but the primary still manages the link.',
                      'Only ABM treats the two stations as equal peers.'],
  misconceptions=[None,'Thinks polling gives both sides equal rights','Confuses "secondary may initiate" with equal peers','Assumes all modes are symmetric'],
  explanation='The modes differ in who may start a transmission: NRM after a poll, ARM the secondary too, ABM both stations as peers.')
Q.append(q)

# structural self-check (generator self-check, not validation)
for q in Q:
    for key in ('answers',):
        if key in q:
            n = len(q['answers'])
            assert len(q['optionExplanations']) == n and len(q['misconceptions']) == n
            assert all(0 <= c < n for c in q['correct'])
    if q['type'] == 'ordering':
        assert sorted(q['correctOrder']) == list(range(len(q['items']))) and q['correctOrder'] != list(range(len(q['items'])))
    if q['type'] == 'matching':
        assert [m[1] for m in q['matches']] != list(range(len(q['matches'])))
    if q['type'] == 'two_tier':
        for t in ('answerTier', 'reasonTier'):
            n = len(q[t]['answers']); assert len(q[t]['optionExplanations']) == n == len(q[t]['misconceptions'])
    pass

def tiers(q):
    if 'answers' in q: return [('main', q)]
    if q['type'] == 'two_tier': return [('answer', q['answerTier']), ('reason', q['reasonTier'])]
    return []
def cue(t):
    """Per-question length cue: the correct option(s) stand out as longer than every distractor."""
    L = [len(a) for a in t['answers']]; right = [L[i] for i in t['correct']]
    wrong = [L[i] for i in range(len(L)) if i not in t['correct']]
    if len(right) > 1: return min(right) > max(wrong)
    return right[0] > max(wrong) and right[0] >= 1.2 * (sum(wrong) / len(wrong))
flags = []
for q in Q:
    for name, t in tiers(q):
        if cue(t): flags.append(f"{q['id']} {name}")
checked = sum(len(tiers(q)) for q in Q)
json.dump(Q, open('/root/qm-run/preview-bank.json', 'w'), indent=2, ensure_ascii=False)
print(len(Q), 'questions;', checked, 'choice tiers checked; length cues:', flags or 'none')
from collections import Counter
print(Counter(q['cognitiveRole'] for q in Q), Counter(q['type'] for q in Q))

# -*- coding: utf-8 -*-
import copy

from scapy.layers.inet import IP
from scapy.sendrecv import sendp
from scapy.utils import rdpcap

src_pcap = "/home/frz/PycharmProjects/Project/qt_tools/Attack/data/sip/invite.pcap"
# Read a pcap or pcapng file and return a packet list
pcaps = rdpcap(src_pcap)
"""转义序列"""
print(pcaps[0])
data = "\xf2\xb6\xe9\x2e\x8e\x9d\x00\x0e\x0c\x62\x8c\x8e\x08\x00\x45\x00" \
       "\x05\x3a\x00\x00\x40\x00\x40\x11\xf7\xe7\xc0\xa8\xde\x66\xc0\xa8" \
       "\xde\x13\x13\xc4\x13\xc9\x05\x26\xed\x25\x49\x4e\x56\x49\x54\x45" \
       "\x20\x73\x69\x70\x3a\x33\x30\x30\x31\x40\x31\x39\x32\x2e\x31\x36" \
       "\x38\x2e\x32\x32\x32\x2e\x31\x39\x3a\x35\x30\x36\x35\x3b\x74\x72" \
       "\x61\x6e\x73\x70\x6f\x72\x74\x3d\x55\x44\x50\x3b\x75\x73\x65\x72" \
       "\x3d\x70\x68\x6f\x6e\x65\x20\x53\x49\x50\x2f\x32\x2e\x30\x0d\x0a" \
       "\x46\x72\x6f\x6d\x3a\x20\x22\x35\x30\x30\x30\x32\x22\x3c\x73\x69" \
       "\x70\x3a\x35\x30\x30\x30\x32\x40\x31\x39\x32\x2e\x31\x36\x38\x2e" \
       "\x32\x32\x32\x2e\x31\x30\x32\x3b\x75\x73\x65\x72\x3d\x70\x68\x6f" \
       "\x6e\x65\x3e\x3b\x74\x61\x67\x3d\x61\x34\x37\x38\x39\x63\x34\x38" \
       "\x2d\x30\x2d\x31\x33\x63\x34\x2d\x36\x31\x61\x65\x63\x33\x36\x33" \
       "\x2d\x32\x64\x34\x31\x66\x35\x33\x61\x2d\x36\x31\x61\x65\x63\x33" \
       "\x36\x33\x0d\x0a\x54\x6f\x3a\x20\x3c\x73\x69\x70\x3a\x33\x30\x30" \
       "\x31\x40\x31\x39\x32\x2e\x31\x36\x38\x2e\x32\x32\x32\x2e\x31\x39" \
       "\x3a\x35\x30\x36\x35\x3b\x75\x73\x65\x72\x3d\x70\x68\x6f\x6e\x65" \
       "\x3e\x0d\x0a\x43\x61\x6c\x6c\x2d\x49\x44\x3a\x20\x55\x44\x44\x6c" \
       "\x4d\x74\x6c\x54\x33\x71\x75\x63\x67\x6a\x4a\x6f\x66\x47\x57\x6c" \
       "\x77\x50\x78\x62\x53\x38\x67\x6d\x49\x79\x65\x2d\x31\x36\x33\x38" \
       "\x38\x34\x33\x32\x33\x35\x32\x38\x31\x2d\x30\x78\x38\x31\x36\x66" \
       "\x38\x65\x61\x38\x2d\x30\x30\x30\x65\x30\x63\x36\x32\x38\x63\x38" \
       "\x65\x40\x31\x39\x32\x2e\x31\x36\x38\x2e\x32\x32\x32\x2e\x31\x30" \
       "\x32\x0d\x0a\x43\x53\x65\x71\x3a\x20\x31\x20\x49\x4e\x56\x49\x54" \
       "\x45\x0d\x0a\x56\x69\x61\x3a\x20\x53\x49\x50\x2f\x32\x2e\x30\x2f" \
       "\x55\x44\x50\x20\x31\x39\x32\x2e\x31\x36\x38\x2e\x32\x32\x32\x2e" \
       "\x31\x30\x32\x3a\x35\x30\x36\x30\x3b\x72\x70\x6f\x72\x74\x3b\x62" \
       "\x72\x61\x6e\x63\x68\x3d\x7a\x39\x68\x47\x34\x62\x4b\x2d\x36\x31" \
       "\x61\x65\x63\x33\x36\x33\x2d\x39\x32\x61\x62\x33\x62\x64\x31\x2d" \
       "\x36\x33\x38\x63\x35\x35\x30\x34\x0d\x0a\x55\x73\x65\x72\x2d\x41" \
       "\x67\x65\x6e\x74\x3a\x20\x73\x74\x61\x72\x2d\x6e\x65\x74\x0d\x0a" \
       "\x4d\x61\x78\x2d\x46\x6f\x72\x77\x61\x72\x64\x73\x3a\x20\x37\x30" \
       "\x0d\x0a\x53\x75\x70\x70\x6f\x72\x74\x65\x64\x3a\x20\x31\x30\x30" \
       "\x72\x65\x6c\x2c\x72\x65\x70\x6c\x61\x63\x65\x73\x2c\x69\x6e\x2d" \
       "\x62\x61\x6e\x64\x2d\x64\x74\x6d\x66\x2c\x74\x69\x6d\x65\x72\x2c" \
       "\x50\x2d\x45\x61\x72\x6c\x79\x2d\x4d\x65\x64\x69\x61\x2c\x31\x30" \
       "\x30\x72\x65\x6c\x2c\x74\x69\x6d\x65\x72\x2c\x72\x65\x70\x6c\x61" \
       "\x63\x65\x73\x2c\x69\x6e\x2d\x62\x61\x6e\x64\x2d\x64\x74\x6d\x66" \
       "\x0d\x0a\x50\x2d\x45\x61\x72\x6c\x79\x2d\x4d\x65\x64\x69\x61\x3a" \
       "\x20\x73\x75\x70\x70\x6f\x72\x74\x65\x64\x2c\x73\x75\x70\x70\x6f" \
       "\x72\x74\x65\x64\x0d\x0a\x43\x6f\x6e\x74\x61\x63\x74\x3a\x20\x3c" \
       "\x73\x69\x70\x3a\x35\x30\x30\x30\x32\x40\x31\x39\x32\x2e\x31\x36" \
       "\x38\x2e\x32\x32\x32\x2e\x31\x30\x32\x3a\x35\x30\x36\x30\x3b\x74" \
       "\x72\x61\x6e\x73\x70\x6f\x72\x74\x3d\x55\x44\x50\x3e\x0d\x0a\x53" \
       "\x65\x73\x73\x69\x6f\x6e\x2d\x45\x78\x70\x69\x72\x65\x73\x3a\x20" \
       "\x39\x30\x30\x0d\x0a\x4d\x69\x6e\x2d\x53\x45\x3a\x20\x39\x30\x0d" \
       "\x0a\x41\x6c\x6c\x6f\x77\x3a\x20\x49\x4e\x56\x49\x54\x45\x2c\x41" \
       "\x43\x4b\x2c\x42\x59\x45\x2c\x43\x41\x4e\x43\x45\x4c\x2c\x50\x52" \
       "\x41\x43\x4b\x2c\x49\x4e\x46\x4f\x2c\x52\x45\x47\x49\x53\x54\x45" \
       "\x52\x2c\x55\x50\x44\x41\x54\x45\x2c\x4f\x50\x54\x49\x4f\x4e\x53" \
       "\x2c\x52\x45\x46\x45\x52\x0d\x0a\x43\x6f\x6e\x74\x65\x6e\x74\x2d" \
       "\x54\x79\x70\x65\x3a\x20\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f" \
       "\x6e\x2f\x73\x64\x70\x0d\x0a\x43\x6f\x6e\x74\x65\x6e\x74\x2d\x4c" \
       "\x65\x6e\x67\x74\x68\x3a\x20\x35\x30\x36\x0d\x0a\x0d\x0a\x76\x3d" \
       "\x30\x0d\x0a\x6f\x3d\x53\x6f\x66\x74\x53\x57\x49\x54\x43\x48\x20" \
       "\x31\x36\x33\x38\x38\x34\x33\x32\x33\x35\x20\x31\x36\x33\x38\x38" \
       "\x34\x33\x32\x33\x35\x20\x49\x4e\x20\x49\x50\x34\x20\x31\x39\x32" \
       "\x2e\x31\x36\x38\x2e\x32\x32\x32\x2e\x31\x30\x32\x0d\x0a\x73\x3d" \
       "\x53\x6f\x66\x74\x53\x57\x49\x54\x43\x48\x0d\x0a\x63\x3d\x49\x4e" \
       "\x20\x49\x50\x34\x20\x31\x39\x32\x2e\x31\x36\x38\x2e\x32\x32\x32" \
       "\x2e\x31\x30\x32\x0d\x0a\x74\x3d\x30\x20\x30\x0d\x0a\x6d\x3d\x61" \
       "\x75\x64\x69\x6f\x20\x34\x30\x37\x37\x38\x20\x52\x54\x50\x2f\x41" \
       "\x56\x50\x20\x39\x20\x38\x20\x30\x20\x31\x30\x31\x0d\x0a\x62\x3d" \
       "\x41\x53\x3a\x36\x34\x0d\x0a\x61\x3d\x72\x74\x70\x6d\x61\x70\x3a" \
       "\x31\x30\x31\x20\x74\x65\x6c\x65\x70\x68\x6f\x6e\x65\x2d\x65\x76" \
       "\x65\x6e\x74\x2f\x38\x30\x30\x30\x0d\x0a\x61\x3d\x66\x6d\x74\x70" \
       "\x3a\x31\x30\x31\x20\x30\x2d\x31\x35\x0d\x0a\x61\x3d\x73\x65\x6e" \
       "\x64\x72\x65\x63\x76\x0d\x0a\x6d\x3d\x76\x69\x64\x65\x6f\x20\x34" \
       "\x30\x37\x38\x30\x20\x52\x54\x50\x2f\x41\x56\x50\x20\x31\x30\x34" \
       "\x20\x31\x30\x38\x0d\x0a\x62\x3d\x41\x53\x3a\x33\x30\x37\x32\x0d" \
       "\x0a\x61\x3d\x72\x74\x70\x6d\x61\x70\x3a\x31\x30\x38\x20\x48\x32" \
       "\x36\x35\x2f\x39\x30\x30\x30\x30\x0d\x0a\x61\x3d\x72\x74\x70\x6d" \
       "\x61\x70\x3a\x31\x30\x34\x20\x48\x32\x36\x34\x2f\x39\x30\x30\x30" \
       "\x30\x0d\x0a\x61\x3d\x66\x6d\x74\x70\x3a\x31\x30\x38\x20\x70\x72" \
       "\x6f\x66\x69\x6c\x65\x2d\x69\x64\x3d\x31\x3b\x6c\x65\x76\x65\x6c" \
       "\x2d\x69\x64\x3d\x31\x32\x30\x0d\x0a\x61\x3d\x66\x6d\x74\x70\x3a" \
       "\x31\x30\x34\x20\x70\x72\x6f\x66\x69\x6c\x65\x2d\x6c\x65\x76\x65" \
       "\x6c\x2d\x69\x64\x3d\x34\x32\x65\x30\x32\x38\x3b\x6d\x61\x78\x2d" \
       "\x62\x72\x3d\x37\x36\x38\x30\x3b\x6d\x61\x78\x2d\x6d\x62\x70\x73" \
       "\x3d\x32\x34\x35\x37\x36\x30\x3b\x6d\x61\x78\x2d\x66\x73\x3d\x38" \
       "\x31\x39\x32\x3b\x70\x61\x63\x6b\x65\x74\x69\x7a\x61\x74\x69\x6f" \
       "\x6e\x2d\x6d\x6f\x64\x65\x3d\x31\x0d\x0a\x61\x3d\x72\x74\x63\x70" \
       "\x2d\x66\x62\x3a\x2a\x20\x63\x63\x6d\x20\x66\x69\x72\x0d\x0a\x61" \
       "\x3d\x72\x74\x63\x70\x2d\x66\x62\x3a\x2a\x20\x6e\x61\x63\x6b\x0d" \
       "\x0a\x61\x3d\x72\x74\x63\x70\x2d\x66\x62\x3a\x2a\x20\x63\x63\x6d" \
       "\x20\x74\x6d\x6d\x62\x72\x0d\x0a"
"""十六进制流"""
# f2b6e92e8e9d000e0c628c8e08004500053a000040004011f7e7c0a8de66c0a8de1313c413c90526ed25494e56495445207369703a33303031403139322e3136382e3232322e31393a353036353b7472616e73706f72743d5544503b757365723d70686f6e65205349502f322e300d0a46726f6d3a20223530303032223c7369703a3530303032403139322e3136382e3232322e3130323b757365723d70686f6e653e3b7461673d61343738396334382d302d313363342d36316165633336332d32643431663533612d36316165633336330d0a546f3a203c7369703a33303031403139322e3136382e3232322e31393a353036353b757365723d70686f6e653e0d0a43616c6c2d49443a205544446c4d746c5433717563676a4a6f6647576c775078625338676d4979652d313633383834333233353238312d307838313666386561382d303030653063363238633865403139322e3136382e3232322e3130320d0a435365713a203120494e564954450d0a5669613a205349502f322e302f554450203139322e3136382e3232322e3130323a353036303b72706f72743b6272616e63683d7a39684734624b2d36316165633336332d39326162336264312d36333863353530340d0a557365722d4167656e743a20737461722d6e65740d0a4d61782d466f7277617264733a2037300d0a537570706f727465643a2031303072656c2c7265706c616365732c696e2d62616e642d64746d662c74696d65722c502d4561726c792d4d656469612c31303072656c2c74696d65722c7265706c616365732c696e2d62616e642d64746d660d0a502d4561726c792d4d656469613a20737570706f727465642c737570706f727465640d0a436f6e746163743a203c7369703a3530303032403139322e3136382e3232322e3130323a353036303b7472616e73706f72743d5544503e0d0a53657373696f6e2d457870697265733a203930300d0a4d696e2d53453a2039300d0a416c6c6f773a20494e564954452c41434b2c4259452c43414e43454c2c505241434b2c494e464f2c52454749535445522c5550444154452c4f5054494f4e532c52454645520d0a436f6e74656e742d547970653a206170706c69636174696f6e2f7364700d0a436f6e74656e742d4c656e6774683a203530360d0a0d0a763d300d0a6f3d536f66745357495443482031363338383433323335203136333838343332333520494e20495034203139322e3136382e3232322e3130320d0a733d536f66745357495443480d0a633d494e20495034203139322e3136382e3232322e3130320d0a743d3020300d0a6d3d617564696f203430373738205254502f415650203920382030203130310d0a623d41533a36340d0a613d7274706d61703a3130312074656c6570686f6e652d6576656e742f383030300d0a613d666d74703a31303120302d31350d0a613d73656e64726563760d0a6d3d766964656f203430373830205254502f41565020313034203130380d0a623d41533a333037320d0a613d7274706d61703a31303820483236352f39303030300d0a613d7274706d61703a31303420483236342f39303030300d0a613d666d74703a3130382070726f66696c652d69643d313b6c6576656c2d69643d3132300d0a613d666d74703a3130342070726f66696c652d6c6576656c2d69643d3432653032383b6d61782d62723d373638303b6d61782d6d6270733d3234353736303b6d61782d66733d383139323b7061636b6574697a6174696f6e2d6d6f64653d310d0a613d727463702d66623a2a2063636d206669720d0a613d727463702d66623a2a206e61636b0d0a613d727463702d66623a2a2063636d20746d6d62720d0a
pcap = copy.deepcopy(pcaps[0])
# print(pcap)
print(pcap[IP].src, type(pcap[IP].src))
pcap[IP].src = '192.0.2.1'
pcap[IP].dst = '11.22.33.44'
# sendp(pcap, iface='enp1s0')

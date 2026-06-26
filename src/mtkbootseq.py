#!/usr/bin/env python3

# Simple utility to request boot modes through the MediaTek (MTK) Preloader
# serial interface.
#
# Compatible with some MediaTek-based phones and tablets whose Preloader
# implements these boot sequences (e.g. MT6572 and other MTK SoCs).
#
# Tested on:
#   - TCL 40 SE
#
# Usage:   python3 mtk-bootseq.py <BOOT_MODE> <SERIAL_PORT>
#
# Example:
#   python3 mtk-bootseq.py FASTBOOT /dev/ttyUSB0
#
# Supported boot mode commands are device/preloader dependent:
#   FASTBOOT  - Enter Fastboot mode
#   METAMETA  - Enter MAUI META mode
#   FACTFACT  - Enter Factory Menu
#   FACTORYM  - Enter Factory Test mode
#   ADVEMETA  - Device-dependent

import sys
import time
from serial import Serial

BOOTSEQ = bytes(sys.argv[1], "ascii")
DEVICE = sys.argv[2]
CONFIRM = b"READY" + BOOTSEQ[:-4:-1]

while True:
    try:
        s = Serial(DEVICE, 115200)
        sys.stdout.write("\n")
        break
    except OSError as e:
        sys.stdout.write("."); sys.stdout.flush()
        time.sleep(0.1)
while True:
    s.write(BOOTSEQ)
    resp = s.read(8)
    print(resp)
    if resp == CONFIRM:
        break
print("Boot sequence sent")

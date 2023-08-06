#!/usr/bin/env python3
#
# Filename: scanner.py
#
# Author: Simon Redman <simon@ergotech.com>
# File Created: 03.03.2023
# Description: Functionality to scan for BLE devices which should be compatible with the rest of this module

import asyncio

from bleak import BleakScanner
from bleak.backends.device import BLEDevice

from typing import Any

from .suta_ble_consts import BedCharacteristic, IS_LINUX, BED_LOCAL_NAME

def build_scanner_kwargs(adapter: str | None = None) -> dict[str, Any]:
    """Add Adapter to kwargs for scanner if specified and using BlueZ."""
    if adapter and IS_LINUX is not True:
        raise ValueError('The adapter option is only valid for the Linux BlueZ Backend.')
    return {'adapter': adapter} if adapter else {}

async def discover(mac: str | None, adapter: str | None = None, wait: int = 5) -> list[BLEDevice]:
    '''
    Scan for devices which expose the interface we expect.
    Do not attempt to connect.
    '''
    scanner_kwargs = build_scanner_kwargs(adapter)
    async with BleakScanner() as scanner:
        await asyncio.sleep(wait)
        if mac:
            mac = mac.lower()
            return [d for d in scanner.discovered_devices if d.address.lower() == mac]
        else:
            devices_and_advertisements = scanner.discovered_devices_and_advertisement_data
            return [d for d, a in devices_and_advertisements.values() if a.local_name == BED_LOCAL_NAME]
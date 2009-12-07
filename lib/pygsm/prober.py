#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

def probe():
    """Searches for probable ports on the system"""
    import platform
    from gsmmodem import GsmModem
    import serial
    ports = []

    if platform.system() == "Linux":
        import scanlinux as portscanner
    if platform.system() == "Windows":
        import scanwin32 as portscanner
    if platform.system() == "Darwin":
        import scanmac as portscanner

    try:
        for port in portscanner.scan():
            try:
                GsmModem(port=port, timeout=10, baudrate=115200, logger=logger)
                ports.append(port)
            except serial.serialutil.SerialException, e:
                pass
    except NameError, e:
        pass
    return ports

def logger(_modem, message_, type_):
    """Supress all output from pySerial and gsmmodem"""
    pass

if __name__ == "__main__":
    print "\n".join(probe())

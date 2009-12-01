#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

def probe():
    """Searches for probable ports on the system"""
    import platform
    from gsmmodem import GsmModem
    import serial
    ports = []
    if platform.system() == "Linux" :
        import scanlinux
        for port in scanlinux.scan():
            try:
                modem = GsmModem(port=port, logger = logger)
                ports.append(port)
            except serial.serialutil.SerialException:
                pass
        return ports

    if platform.system() == "Windows" :
        import scanwin32
        for port in scanwin32.scan():
            try:
                modem = GsmModem(port=port, logger = logger)
                ports.append(port)
            except serial.serialutil.SerialException:
                pass

def logger(_modem, message_, type_):
    """This just disables debug"""
    pass


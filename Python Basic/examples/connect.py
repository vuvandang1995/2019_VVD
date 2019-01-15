# Example-3.py
from __future__ import print_function
import sys
import libvirt
SASL_USER = "dangvv"
SASL_PASS = "1"
def request_cred(credentials, user_data):
 for credential in credentials:
    if credential[0] == libvirt.VIR_CRED_AUTHNAME:
        credential[4] = SASL_USER
    elif credential[0] == libvirt.VIR_CRED_PASSPHRASE:
        credential[4] = SASL_PASS
 return 0
auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_PASSPHRASE], request_cred, None]
conn = libvirt.openAuth('qemu+tcp://192.168.40.138/system', auth, 0)
host = conn.getHostname()
if conn == None:
 print('Failed to open connection to qemu+tcp://localhost/system', file=sys.stderr)
 exit(1)
conn.close()
exit(0)

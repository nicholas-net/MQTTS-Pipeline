import ipaddress
from datetime import datetime, timedelta, timezone
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

"""
ipaddress - adding ipv4/ipv6 to a certificate
datetime, timedelta, timezone - setting "valid from" and "valid until" dates
Path - for path file handling
"""

def generate_key(self):

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)


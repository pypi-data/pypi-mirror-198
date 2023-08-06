import os
from typing import List

import certifi
import logging

certificate_dir = os.path.join(os.path.dirname(__file__), "certificates")


def _get_certificates() -> List[str]:
    path = certifi.where()
    # Get current certificates.
    with open(path, 'r') as f:
        certs = f.readlines()
    # Create backup.
    logging.info(f"Saving backup to [{path}.bak]")
    with open(path + ".bak", 'w') as f:
        f.writelines(certs)
    return certs


def _write_certificates(certs: List[str]):
    path = certifi.where()
    logging.info(f"Writing certificates to {path}")
    with open(path, 'w') as f:
        f.writelines(certs)


def _add_vestas_certificates(certs: List[str]):
    logging.info(f"Updating with certificates in {certificate_dir}")
    for item in os.listdir(certificate_dir):
        src = os.path.join(certificate_dir, item)
        if os.path.isdir(src):
            continue
        if src[-4:] != ".crt":
            continue
        with open(src, 'r') as f:
            cert = f.readlines()
            certs.extend(["\n", "# Source: " + item + "\n"])
            certs.extend(cert)
            logging.info(f"Added certificate {item} ")
    return certs


def _delete_vestas_certificates(certs):
    for item in os.listdir(certificate_dir):
        src = os.path.join(certificate_dir, item)
        if os.path.isfile(src) and src.split('.')[-1] == 'crt':
            with open(src, 'r') as f:
                cert = f.readlines()
            i = 0
            while i < len(certs) - len(cert) + 1:
                if certs[i:i + len(cert)] == cert:
                    ii, ie = i, i + len(cert) - 1
                    ii = ii - 1 if "# Source: " in certs[ii - 1] else ii
                    ii = ii - 1 if '' == certs[ii - 1].strip() else ii
                    logging.info(f"Removing certificate {item}")
                    del certs[ii:ie + 1]
                    i = ii - 1
                i += 1
    return certs


def _has_certificates():
    with open(certifi.where()) as f_bundle:
        bundle = f_bundle.read()
        for item in os.listdir(certificate_dir):
            src = os.path.join(certificate_dir, item)
            if item.endswith(".crt"):
                with open(src) as cert:
                    if cert.read() not in bundle:
                        return False
    return True


# region Public interface

def add_certificates():
    """
    Add Vestas certificates.
    """
    certs = _get_certificates()
    certs = _add_vestas_certificates(certs)
    _write_certificates(certs)


def del_certificates():
    """
    Delete Vestas certificates (if they are present).
    """
    certs = _get_certificates()
    certs = _delete_vestas_certificates(certs)
    _write_certificates(certs)


def fix_ssl_error():
    """
    Inject Vestas certificates if they are not already present.
    """
    if not _has_certificates():
        logging.info("No Vestas certificates found - adding.")
        add_certificates()

# endregion

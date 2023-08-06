import argparse
from vespy import *

parser = argparse.ArgumentParser(
    usage='%(prog)s [options]',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""Utility package to install SSL certificates for Vestas firewalls""",
    add_help=True
)
parser.add_argument('--fix-ssl',
                    help=f"Add SSL ca-certificates to system",
                    dest='fixssl',
                    action='store_true',
                    default=False,
                    )
parser.add_argument('--del-ssl',
                    help=f"Delete SSL ca-certificates from system",
                    dest='delssl',
                    action='store_true',
                    default=False,
                    )


def run():
    args = parser.parse_args()
    if args.fixssl and args.delssl:
        parser.print_help()
        raise RuntimeError("Both '--fix-ssl' and '--del-ssl' given, please provide only one...")
    elif args.fixssl:
        fix_ssl_error()
    elif args.delssl:
        del_certificates()
    else:
        parser.print_help()

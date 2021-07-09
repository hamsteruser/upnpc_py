import argparse
import upnpc

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', required=True,
                        help='mapport, unmapport, unmapall, used')
    parser.add_argument('-p', '--port', type=int, default=None, required=False)
    parser.add_argument('-r', '--proto', type=str, default="TCP", required=False)
    args = parser.parse_args()

    upnp = upnpc.port_manager()
    if args.action == 'mapport':
        result = upnp.mapport(args.port, args.proto)
        print(result)
    elif args.action == 'unmapport':
        if not args.port:
            print("Port argument required")
            exit(1)
        result = upnp.unmapport(args.port, args.proto)
        print(result)
    elif args.action == 'unmapall':
        upnp.unmap_allports()
    elif args.action == 'used':
        upnp.used_ports()

main()

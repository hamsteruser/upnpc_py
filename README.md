# Library that's maps and unmaps upnp ports.

## class name is port_manager.

## Class arguments:

## Methods:
* `discover` check current upnp status. Returns ValueError Exception if unavailable.
* `unmap_allports` unmap all ports.
* `mapport` map the port. Arguments ['port', 'proto']. Port will be random if port=None here. Default proto is TCP.
            returns boolean and str port
* `unmapport` unmap the port Arguments ['port', 'proto']. Default proto is TCP.

from .ds_service_discovery_dns_namespace import DsServiceDiscoveryDnsNamespace
from .ds_service_discovery_http_namespace import DsServiceDiscoveryHttpNamespace
from .ds_service_discovery_service import DsServiceDiscoveryService
from .service_discovery_http_namespace import ServiceDiscoveryHttpNamespace
from .service_discovery_instance import ServiceDiscoveryInstance
from .service_discovery_private_dns_namespace import ServiceDiscoveryPrivateDnsNamespace
from .service_discovery_public_dns_namespace import ServiceDiscoveryPublicDnsNamespace
from .service_discovery_service import ServiceDiscoveryService

__all__ = [
    "ServiceDiscoveryService",
    "ServiceDiscoveryInstance",
    "ServiceDiscoveryHttpNamespace",
    "ServiceDiscoveryPrivateDnsNamespace",
    "ServiceDiscoveryPublicDnsNamespace",
    "DsServiceDiscoveryHttpNamespace",
    "DsServiceDiscoveryService",
    "DsServiceDiscoveryDnsNamespace",
]

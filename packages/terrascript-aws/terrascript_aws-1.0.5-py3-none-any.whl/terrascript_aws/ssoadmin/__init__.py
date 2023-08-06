from .account_assignment import AccountAssignment
from .ds_instances import DsInstances
from .ds_permission_set import DsPermissionSet
from .managed_policy_attachment import ManagedPolicyAttachment
from .permission_set import PermissionSet
from .permission_set_inline_policy import PermissionSetInlinePolicy

__all__ = [
    "PermissionSetInlinePolicy",
    "PermissionSet",
    "ManagedPolicyAttachment",
    "AccountAssignment",
    "DsPermissionSet",
    "DsInstances",
]

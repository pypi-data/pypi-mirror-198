from .access_key import AccessKey
from .account_alias import AccountAlias
from .account_password_policy import AccountPasswordPolicy
from .ds_account_alias import DsAccountAlias
from .ds_group import DsGroup
from .ds_instance_profile import DsInstanceProfile
from .ds_instance_profiles import DsInstanceProfiles
from .ds_openid_connect_provider import DsOpenidConnectProvider
from .ds_policy import DsPolicy
from .ds_policy_document import DsPolicyDocument
from .ds_role import DsRole
from .ds_roles import DsRoles
from .ds_server_certificate import DsServerCertificate
from .ds_session_context import DsSessionContext
from .ds_user import DsUser
from .ds_user_ssh_key import DsUserSshKey
from .ds_users import DsUsers
from .group import Group
from .group_membership import GroupMembership
from .group_policy import GroupPolicy
from .group_policy_attachment import GroupPolicyAttachment
from .instance_profile import InstanceProfile
from .openid_connect_provider import OpenidConnectProvider
from .policy import Policy
from .policy_attachment import PolicyAttachment
from .role import Role
from .role_policy import RolePolicy
from .role_policy_attachment import RolePolicyAttachment
from .saml_provider import SamlProvider
from .server_certificate import ServerCertificate
from .service_linked_role import ServiceLinkedRole
from .service_specific_credential import ServiceSpecificCredential
from .signing_certificate import SigningCertificate
from .user import User
from .user_group_membership import UserGroupMembership
from .user_login_profile import UserLoginProfile
from .user_policy import UserPolicy
from .user_policy_attachment import UserPolicyAttachment
from .user_ssh_key import UserSshKey
from .virtual_mfa_device import VirtualMfaDevice

__all__ = [
    "InstanceProfile",
    "UserPolicy",
    "GroupMembership",
    "UserSshKey",
    "SigningCertificate",
    "OpenidConnectProvider",
    "Role",
    "AccountAlias",
    "ServerCertificate",
    "Policy",
    "AccountPasswordPolicy",
    "GroupPolicy",
    "GroupPolicyAttachment",
    "ServiceLinkedRole",
    "VirtualMfaDevice",
    "User",
    "ServiceSpecificCredential",
    "SamlProvider",
    "RolePolicy",
    "AccessKey",
    "UserPolicyAttachment",
    "PolicyAttachment",
    "UserLoginProfile",
    "UserGroupMembership",
    "Group",
    "RolePolicyAttachment",
    "DsSessionContext",
    "DsUserSshKey",
    "DsRoles",
    "DsPolicy",
    "DsPolicyDocument",
    "DsUsers",
    "DsOpenidConnectProvider",
    "DsUser",
    "DsInstanceProfiles",
    "DsGroup",
    "DsRole",
    "DsInstanceProfile",
    "DsAccountAlias",
    "DsServerCertificate",
]

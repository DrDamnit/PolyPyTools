from poly_py_tools.pjsip_resource import SipResource


class Aor(SipResource):
    contact = None
    default_expiration = None
    mailboxes = None
    maximum_expiration = None
    max_contacts = None
    minimum_expiration = None
    remove_existing = None
    type = None
    qualify_frequency = None
    authenticate_qualify = None
    outbound_proxy = None
    support_path = None
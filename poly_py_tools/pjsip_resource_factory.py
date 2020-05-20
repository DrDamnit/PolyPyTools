from poly_py_tools.pjsip_endpoint import Endpoint
from poly_py_tools.pjsip_transport import Transport
from poly_py_tools.pjsip_auth import Auth
from poly_py_tools.pjsip_aor import Aor
from poly_py_tools.pjsip_registration import Registration
from poly_py_tools.pjsip_domain_alias import DomainAlias
from poly_py_tools.pjsip_acl import Acl
from poly_py_tools.pjsip_contact import Contact

class SipResourceFactory:

    def __init__(self):
        pass

    def create(self, section):
        type = self.extract_type(section)

        if type == "endpoint":
            return Endpoint(section)

        if type == "transport":
            return Transport(section)

        if type == "auth":
            return Auth(section)

        if type == "aor":
            return Aor(section)

        if type == "registration":
            return Registration(section)

        if type == "domain_alias":
            return DomainAlias(section)

        if type == "acl":
            return Acl(section)

        if type == "contact":
            return Contact(section)

    def extract_type(self, section):

        for line in section:
            if not "=" in line:
                continue

            option, value = line.split("=")
            if option == "type":
                return str(value).lower()

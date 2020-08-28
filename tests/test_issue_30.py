import unittest
import os
import shutil

from unittest_data_provider import data_provider

from poly_py_tools.polypy_config import PolypyConfig
from poly_py_tools.provision_factory import ProvisionFactory

class TestIssue30(unittest.TestCase):

    def setUp(self) -> None:
        self.clean_files()

    def tearDown(self) -> None:
        self.clean_files()

    def clean_files(self):
        files = ['0004f23a43bf.cfg', 'some-site-template/0004f23a43bf']
        dirs = ['some-site-template']
        for f in files:
            target_file = os.path.join(self.get_tftproot(), f)
            if os.path.exists(target_file):
                os.remove(target_file)
        for d in dirs:
            target_dir = os.path.join(self.get_tftproot(), d)
            if os.path.exists(target_dir):
                os.rmdir(target_dir)

    def get_tftproot(self):
        return os.path.join(os.path.dirname(__file__), "fixtures/fs")

    provider_test_issue_30 = lambda : (
        ("0004f23a43bf", "0004f23a43bf",),
        ("00:04:f2:3a:43:bf", "0004f23a43bf",),
        ("00-04-f2-3a-43-bf", "0004f23a43bf",),
        ("0004F23A43BF", "0004f23a43bf",),
        ("00:04:F2:3A:43:BF", "0004f23a43bf",),
        ("00-04-F2-3A-43-BF", "0004f23a43bf",),
    )

    @data_provider(provider_test_issue_30)
    def test_issue_30(self, mac_address, expected_mac):

        args = {'--force': False,
                 '-d': True,
                 '-v': 0,
                 '<csvfile>': [],
                 '<macaddress>': mac_address,
                 'directory': False,
                 'endpoints': False,
                 'for': False,
                 'list': False,
                 'polycom': True,
                 'provision': True,
                 'using': False}

        fixture_directory = os.path.join(os.path.dirname(__file__), "fixtures/provision_polycom")

        pconf = PolypyConfig()
        pconf.add_search_path(fixture_directory)
        pconf.load()

        pconf.json['paths']['asterisk'] = fixture_directory
        pconf.json['paths']['tftproot'] = self.get_tftproot()

        args['config'] = pconf
        args['<args>'] = args

        factory = ProvisionFactory()
        runner = factory.get_runner(args)
        runner.run()


if __name__ == '__main__':
    unittest.main()
import os
import json
import site
from shutil import copyfile

class PolypyConfig:

    config_path = None
    search_paths = []
    polycom_files = []

    def __init__(self):
        self.polycom_files = ['000000000000.cfg', '000000000000-directory~.xml', "Config/applications.cfg", "Config/device.cfg",
                     "Config/features.cfg", "Config/H323.cfg", "Config/polycomConfig.xsd", "Config/reg-advanced.cfg",
                     "Config/reg-basic.cfg", "Config/region.cfg", "Config/sip-basic.cfg", "Config/sip-interop.cfg",
                     "Config/site.cfg", "Config/video.cfg", "Config/video-integration.cfg"]

    def find(self):
        for path in self.search_paths:
            config_path = os.path.join(path, "polypy.conf")
            if os.path.exists(config_path):
                self.config_path = config_path
                return True

        return False

    def add_search_path(self, path):
        self.search_paths.append(path)

    def load(self):
        with open(self.config_path) as fp:
            self.config = json.load(fp)

    def write(self):
        try:
            with open(self.config_path, 'w') as fp:
                json.dump(self.config,fp)
        except PermissionError:
            print("Could not write config to {}. Perhaps you need to be root?".format(self.config_path))
            raise PermissionError

    def write_default_config(self, target_path):
        self.config_path = target_path
        configs = {}
        # Setup default values:
        lib_path = '/var/lib/polypy'
        share_path = '/usr/share/polypy/'
        local_bin = '/usr/local/bin/'
        package_path = None

        paths = {}

        package_path = os.path.join(site.getsitepackages()[0], 'poly_py_tools')

        paths["asterisk"] = "/etc/asterisk/"
        paths["tftproot"] = "/srv/tftp/"
        configs['lib_path'] = lib_path
        configs['share_path'] = share_path
        configs['config_path'] = self.config_path
        configs['package_path'] = package_path
        configs['paths'] = paths
        configs['server_addr'] = "127.0.0.1"
        self.config = configs

        self.write()

    def set_path(self, path, target_path):
        if target_path is ".":
            target_path = os.getcwd()

        if not str(target_path).startswith("/"):
            target_path = os.path.join(os.getcwd(), target_path)

        self.config['paths'][path] = target_path
        self.write()

    def set_server(self, server_addr):
        self.config['server_addr'] = server_addr
        self.write()

    def validate(self):
        state_report = {}
        state_report[self.config['paths']['asterisk']] = os.path.exists(os.path.join(self.config['paths']['asterisk'], "sip.conf"))
        state_report[self.config['paths']['tftproot']] = os.path.exists(self.config['paths']['tftproot'])

        for file in self.polycom_files:
            target_path = os.path.join(self.config['paths']['tftproot'], file)
            state_report[target_path] = os.path.exists(target_path)

        if False in state_report.values():
            print("The following files could not be found. Consider running copy-files to fix this.")
            for path in state_report:
                if state_report[path] == False:
                    print(path)
        else:
            print("Configuration looks good.")

        return state_report

    def copy_files(self, source_path):

        if not os.path.exists(source_path):
            print("Path %s does not exist. Quitting." % source_path)
            exit(1)

        missing_files = []

        for file in self.polycom_files:
            target_path = os.path.join(source_path, file)
            if not os.path.exists(target_path):
                missing_files.append(target_path)

        if len(missing_files) > 0:
            print("Some required files are missing from {}".format(source_path))
            for file in missing_files:
                print("- {}".format(file))

            exit(1)

        # Copy everything over.

        target_path = os.path.join(os.getcwd(), 'tftp')
        target_path = self.config['paths']['tftproot']

        if not os.path.exists(target_path):
            os.mkdir(target_path)

        target_config_path = os.path.join(target_path, "Config")
        if not os.path.exists(target_config_path):
            os.mkdir(target_config_path)

        for file in self.polycom_files:
            source_file = os.path.join(source_path, file)
            target_file = os.path.join(target_path, file)
            print("Copying: {} => {}".format(source_file, target_file))
            copyfile(source_file, target_file)
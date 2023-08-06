class TestCopilot:
    def __init__(self):
        pass

    def run_bdio_from_package_manager(self):
        """
        Runs bdio generation from package manager
        """
        pkg_detector = PkgDetector()
        pkg_detector.get_platform()
        logging.info("Package manager is: {}".format(pkg_detector.package_manager))
        logging.info("OS distribution is: {}".format(pkg_detector.os_distribution))
        if pkg_detector.package_manager == 'rpm':
            rpm_bdio = RpmBdioGenerator(pkg_detector.os_distribution)
            rpm_bdio.generate_bdio()
        elif pkg_detector.package_manager == 'dpkg':
            dpkg_bdio = DpkgBdioGenerator(pkg_detector.os_distribution)
            dpkg_bdio.generate_bdio()
        else:
            logging.info("Package manager not found. Skipping bdio generation from package manager")

    def DpkgBdioGenerator(self, os_distribution):
"""
        Generates bdio from dpkg
        """
        dpkg_bdio = DpkgBdioGenerator(os_distribution)
        dpkg_bdio.generate_bdio()

    def generate_bdio(self):



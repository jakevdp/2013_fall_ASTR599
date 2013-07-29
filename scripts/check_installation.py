import warnings
import sys
import os
from distutils.version import StrictVersion

def warn(msg):
    print msg
    warnings.warn(msg)
    warn.count += 1
warn.count = 0


def check_import(package_name, version=None):
    try:
        pkg = __import__(package_name)
    except ImportError:
        warn("Package {0} is not available".format(package_name))
        return

    if version:
        pkg_version = pkg.__version__.rstrip('git').rstrip('-')

        if StrictVersion(str(pkg_version)) < str(version):
            warn("Package {0} is version {1}; "
                 "{2} or greater is recommended".format(pkg, pkg.__version__,
                                                        version))
    

# check Python version
if not (2, 6) <= sys.version_info[:2] <= (2, 7):
    warn("Python 2.6 - 2.7 recommended")


# check package versions
check_import('numpy', '1.5')
check_import('scipy', '0.11')
check_import('IPython', '0.13')
check_import('matplotlib', '1.0')
check_import('sklearn', '0.12')
check_import('nose')


if warn.count > 0:
    print(" - warning count: {0}.".format(warn_count))
    print("   Consider upgrading your Python install:")
    print("   Anaconda is a good all-in-one option: ")
    print("   https://store.continuum.io/".format(warn.count))
else:
    print(" - no warnings: Congratulations!  ")
    print("   Your Python installation appears up-to-date!")
    print(" - please confirm that typing ``ipython notebook`` at your terminal")
    print("   launches a browser window to the IPython dashboard.  If not,")
    print("   then there are other packages which must be installed.  For")
    print("   an easy all-in-one installation, try Anaconda:")
    print("            https://store.continuum.io/")

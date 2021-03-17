import os.path as path
import warnings

from .Parser import Parser
from .bio462_hw1 import bio462_hw1
from .bio462_hw2 import bio462_hw2
from .bio462_hw3 import bio462_hw3
from .bio462_hw4 import bio462_hw4
from .bio462_hw6 import bio462_hw6
from .file_download import download
from .file_download import download_text as _download_text

from .exceptions import BiograderError, NoInternetError, OldPackageVersionWarning


def version():
    """Return version number of biograder package."""
    version = {}
    path_here = path.abspath(path.dirname(__file__))
    version_path = path.join(path_here, "version.py")
    with open(version_path) as fp:
        exec(fp.read(), version)
    return version['__version__']


# The link to download the version file in the home directory of the biograder
version_url = "https://byu.box.com/shared/static/vleywdnhpw034sg1peh85nt9p9pxn7y9.txt"
try:
    remote_version = _download_text(version_url)
except NoInternetError:
    pass
else:
    local_version = version()
    if remote_version != local_version:
        warnings.warn(f"Your version of biograder ({local_version}) is out-of-date. Latest is {remote_version}. Please run 'pip install --upgrade biograder' to update it.", OldPackageVersionWarning, stacklevel=2)

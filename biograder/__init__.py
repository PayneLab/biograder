import os.path as path
import sys
import warnings

from .exceptions import BiograderError, NoInternetError, OldPackageVersionWarning

#from .file_download import download
from .file_download import download_text as _download_text


def version():
    """Return version number of biograder package."""
    version = {}
    path_here = path.abspath(path.dirname(__file__))
    version_path = path.join(path_here, "version.py")
    with open(version_path) as fp:
        exec(fp.read(), version)
    return (version['__version__'])

#FIXME: change this to biograder's version.txt direct link url

version_url = "https://byu.box.com/shared/static/kbwivmqnrdnn5im2gu6khoybk5a3rfl0.txt"
try:
    remote_version = _download_text(version_url)
except NoInternetError:
    pass
else:
    local_version = version()
    if remote_version != local_version:
        warnings.warn(f"Your version of cptac ({local_version}) is out-of-date. Latest is {remote_version}. Please run 'pip install --upgrade cptac' to update it.", OldPackageVersionWarning, stacklevel=2)
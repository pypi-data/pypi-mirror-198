"""Simple extension of various skimage.transform utilites for 3D images."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("skimage3d")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Dennis Brookner"
__email__ = "debrookner@gmail.com"

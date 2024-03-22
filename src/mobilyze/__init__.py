from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("mobilyze")
except PackageNotFoundError:
    # package is not installed
    pass

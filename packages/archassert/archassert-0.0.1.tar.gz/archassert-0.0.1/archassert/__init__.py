# version as tuple for simple comparisons
VERSION = (0, 7, 2)
# string created from tuple to avoid inconsistency
__version__ = ".".join([str(x) for x in VERSION])

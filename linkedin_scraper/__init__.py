from os.path import basename, dirname, isfile

from .company import Company
from .objects import Contact, Education, Experience, Institution
from .person import Person

__version__ = "2.9.0"

import glob

modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = tuple([basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")])

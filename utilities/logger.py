import os
import sys

from rich import print
from rich.columns import Columns

directory = os.listdir(sys.argv[-1])
print(Columns(directory))

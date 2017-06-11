import sys
from subprocess import call

# if hasattr(sys, "real_prefix"):
    # Within virtualenv
call(["source", "env/bin"])
    
# else:
    # try:
        # python -c "import math"
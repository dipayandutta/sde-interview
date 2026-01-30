from insights.core.plugins import rule,make_info
from insights.parsers.uname import Uname

KEY = "KERNEL_VERSION"
CONTENT = "kernel Version: {{ kernel }}"

@rule(Uname)
def report(uname):
    if uname.kernel and uname.kernel.startswith("5.14"):
        return make_info(
            KEY,
            kernel = uname.kernel
        )

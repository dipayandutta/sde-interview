from insights.core.spec_factory import simple_file
from insights.core import Parser
from  insights.core.plugins import parser,rule
from insights import make_pass,make_fail

OSRelease = simple_file(
    "/etc/os-release",
    description="OS Release Information"
)

@parser(OSRelease)
class OSReleaseParser(Parser):
    def parse_content(self,content):
        #self.release=content[2].strip() if content else None
        self.data = {}
        for line in content:
            if "=" in line:
                k,v = line.split("=",1)
                self.data[k] = v.strip().strip('"')
        #self.release = content
@rule(OSReleaseParser)
def report_os_release(rr):
    if not rr:
        return make_fail("/etc/os-release file not exits")
    formatted = "\n".join(f"{k}={v}" for k,v in rr.data.items())
    return make_pass(
        f"Detected OS-Release {formatted}"
    )

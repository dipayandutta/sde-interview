"""
Insights basic plugin:
Read /etc/redhat-release
"""

from insights.core.spec_factory import simple_file
from insights.core import Parser
from insights.core.plugins import parser, rule
from insights import make_pass, make_fail

# ------------------------------------------------------------
# 1. SPEC: collect /etc/redhat-release
# ------------------------------------------------------------

RedhatRelease = simple_file(
    "/etc/redhat-release",
    description="Red Hat release information"
)

# ------------------------------------------------------------
# 2. PARSER: read file content
# ------------------------------------------------------------

@parser(RedhatRelease)
class RedhatReleaseParser(Parser):
    def parse_content(self, content):
        # content is a list of lines
        self.release = content[0].strip() if content else None

# ------------------------------------------------------------
# 3. RULE: report result
# ------------------------------------------------------------

@rule(RedhatReleaseParser)
def report_redhat_release(rr):
    if rr.release:
        return make_pass(
            f"Detected OS release: {rr.release}"
        )

    return make_fail(
        "/etc/redhat-release is empty or missing"
    )


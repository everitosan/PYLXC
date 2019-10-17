"""
Clas of a component to install in lxc
"""
# Modules
from .ConfigValidator import validate


class LXCComponent():
    required = ["name", "gitRepo", "gitBranch"]

    def __init__(self, data):
        validate(self.required, data, raise_exception=True)
        self.name = data.get("name")
        self.gitRepo = data.get("gitRepo")
        self.gitBranch = data.get("gitBranch")
        self.installScripts = data.get("installScripts")

    def get_build_scripts(self):
        paths = [self.name+"/"+script for script in self.installScripts]
        return paths

    def has_install_scripts(self):
        return self.installScripts is not None

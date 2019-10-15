"""
This class is an abstraction to run lxc commands for an specific
conatainer name.
"""
# Python
import subprocess
# LXC
from LXCComponent import LXCComponent
from Paths import PATHS
from Logger import warn

base_dir = PATHS.get("COPY_BASE")


class LXC():
    def __init__(self, image="", name=""):
        self.name = name
        self.image = image
        self.components = []

    def launch(self):

        if self.name == "" or self.image == "":
            raise Exception("Nombre e imagen son requeridos")
        else:
            command = ["lxc", "launch", "images:"+self.image, self.name]
            subprocess.call(command)

    def set_components_path(self, path):
        self.components_path = path
        self.config_set("COMPONENTSPATH", path)

    def config_set(self, key, val):
        command = [
            "lxc", "config", "set", self.name, "environment."+key, val
        ]
        subprocess.call(command)

    def file_push(self, file_path, execute=False):
        """
        Copy a file from host to container.
        If execute flag is set, it will exeute it.
        Returns the index of internal list for future references
        """
        file_name = file_path.split("/")[-1]

        container_file_path = "{}{}".format(base_dir, file_name)
        command = [
            "lxc",
            "file",
            "push",
            file_path,
            "{}{}".format(self.name, container_file_path)
        ]
        subprocess.call(command)
        if execute:
            self.execute(["chmod", "744", container_file_path])
            self.execute([container_file_path])

    def execute_pushed(self, file, extras=[]):
        """
        Takes the index of the file pushed and executes it.
        """
        container_file_path = base_dir+file
        cmd = [container_file_path] + extras
        self.execute(cmd)

    def execute(self, cmd=[]):
        command = ["lxc", "exec", self.name, "--"] + cmd
        warn(str(command))
        subprocess.call(command)

    def add_components(self, components_list):
        for component in components_list:
            lxcc = LXCComponent(component)
            self.components.append(lxcc)

    def clone_components(self):
        for component in self.components:
            self.execute_pushed("GitCloner.sh", [
                component.gitRepo,
                component.gitBranch,
                component.name
            ])

    def install_components(self):
        for component in self.components:
            if component.has_install_scripts():
                for script in component.get_build_scripts():
                    script_path = self.components_path+script
                    warn(script_path)
                    self.execute([script_path])

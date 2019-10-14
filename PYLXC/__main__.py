# Python
from time import sleep
from os import path

# MODULES
from LXC import LXC
from ConfigLoader import loads_json
from Utils import exit

CONTAINER = None


def launch_container(config):
    global CONTAINER
    CONTAINER = LXC(image=config.get("image"), name=config.get("name"))
    try:
        CONTAINER.launch()
    except Exception as e:
        exit(str(e))


def set_envs(env_conf=None):
    if env_conf is not None:
        for prop in env_conf.keys():
            CONTAINER.config_set(prop, env_conf[prop])


def initial_install(initial_scprit=None):

    if initial_scprit is not None:
        sleep(5)
        CONTAINER.file_push(initial_scprit, True)


def process_components(components=[]):
    # import pdb; pdb.set_trace()
    git_cloner_path = "{}/bash/GitCloner.sh".format(
        path.realpath(__file__)[:-11]
    )
    CONTAINER.file_push(git_cloner_path)
    for component in components:
        print(component)
        CONTAINER.execute_pushed("GitCloner.sh", [
            component.get("gitRepo"),
            component.get("gitBranch"),
            component.get("name")
        ])


if __name__ == "__main__":
    # Read condifguration
    config = loads_json("./config.json")

    launch_container(config)
    set_envs(config.get("env"))
    initial_install(config.get("initialScript"))

    process_components(config.get("components"))

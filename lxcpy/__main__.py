# Python
from time import sleep
from os import path

# MODULES
from .Arguments import parse as parse_arguments
from .ConfigLoader import loads_json
from .LXC import LXC
from .Utils import exit, print_banner
from .Logger import info
from .LXCExport import export as export_lxc

CONTAINER = None


def launch_container(config):
    info("Creando contenedor")
    global CONTAINER
    CONTAINER = LXC(image=config.get("image"), name=config.get("name"))
    try:
        CONTAINER.launch()
        CONTAINER.set_components_path(config.get("componentsPath"))
        git_cloner_path = "{}/bash/GitCloner.sh".format(
            path.realpath(__file__)[:-11]
        )
        CONTAINER.file_push(git_cloner_path)
    except Exception as e:
        exit(str(e))


def set_envs(env_conf=None):
    info("Configurando variables de entorno")
    if env_conf is not None:
        for prop in env_conf.keys():
            CONTAINER.config_set(prop, env_conf[prop])


def install(script=None, delay=0):
    if script is not None:
        info("Instalando {}".format(script))
        sleep(delay)
        CONTAINER.file_push(script, True)


def process_components(components=[]):
    """
    Iterate components, clone them, and build them
    """
    info("Instalando componentes")
    CONTAINER.add_components(components)
    CONTAINER.clone_components()
    CONTAINER.install_components()


def create_from(config_file=None):
    if config_file is None:
        config_file = "./config.json"

    # Read condifguration
    config = loads_json(config_file)
    launch_container(config)
    set_envs(config.get("env"))
    install(config.get("initialScript"), 5)

    # Install components and build them
    process_components(config.get("components", []))

    install(config.get("finalScript"))

    info("OK")


def main():
    print_banner()
    args = parse_arguments()
    if args.export:
        export_lxc(args.export)
    else:
        create_from(args.file)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        info("bye bye")

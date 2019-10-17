"""
Export lxc container by name
"""
# Python
import subprocess
from time import time

# Utils
from .Utils import exit
from .Logger import info


def create_image(c_name, s_name, i_name):
    """
    Creates an image from a container
    """
    info("Publicando imagen {}".format(i_name))
    image_command = [
        "lxc", "publish",
        c_name+"/"+s_name,
        "--alias",
        i_name
    ]
    p_res = subprocess.Popen(
        image_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout, stderr = p_res.communicate()
    res = stdout.decode("utf-8")
    return res[38:-1]


def create_snap(c_name, s_name):
    """
    Creates snapshot of a container
    """
    info("Creando snapshot {}".format(s_name))
    snap_command = ["lxc", "snapshot", c_name, s_name]
    p_res = subprocess.Popen(
        snap_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    _, _ = p_res.communicate()


def export(c_name=""):
    if c_name == "":
        exit("No se encuentra el contenedor {}".format(c_name))

    time_stamp = time()
    snapshot_name = "{}_snapshot_{}".format(c_name, time_stamp)
    image_name = "{}_image_{}".format(c_name, time_stamp)

    # Creates snapshot
    create_snap(c_name, snapshot_name)

    # Publish image
    published = create_image(c_name, snapshot_name, image_name)

    info("Exportnado imagen {}".format(published))
    export_command = [
        "lxc",
        "image",
        "export",
        published
    ]

    subprocess.call(export_command)

    info("Terminado :D")

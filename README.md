# LXCPY

|> Python based tool to create and export LXC containers.

# Create
One of the tool porpuses is to install dependencies and build the apps inside the container.


### Config.json
This is the file that the tool will take as a manifest to create the components(GIT repositories).

```json
{
  "name": "WalkSat2",
  "image": "ubuntu/bionic/amd64",
  "componentsPath": "/home/ubuntu/",
  "env": {
    "http_proxy": "http://proxy.web.com:3128",
    "https_proxy": "http://proxy.web.com:3128"
  },
  "initialScript": "./init.sh",
  "finalScript": "./final.sh",
  "components": [{
      "name": "Backend",
      "gitRepo": "https://gitlab.com/repo.git",
      "gitBranch": "master",
      "installScripts": [
        "scripts/dependencies/base.sh",
        "scripts/dependencies/prod.sh",
        "scripts/dependencies/pip.sh",
        "scripts/build/prod.sh"
      ]
    }, {
        "name": "Frontend",
        "gitRepo": "https://gitlab.com/repo.git",
        "gitBranch": "develop"
      }]
}

```
Once you have your **config** file, you can run the following command at the same directory level.
```
LXCPY
```

If you want to specify the file.
```
LXCPY -f path/to/file
```

## Export
Export an already created container.
```
LXCPY -e CONTAINER-NAME
```

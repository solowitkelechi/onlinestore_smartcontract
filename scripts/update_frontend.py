import yaml, json, os, shutil


def update_frontend():
    # send the build folder to react frontend
    copy_folder_to_front_end("./build", "../frontend/src/chain-info")
    # send the brownie-config.yaml file to frontend as .json
    with open("brownie-config.yaml", "r") as brownie_config:
        config_dict = yaml.load(brownie_config, Loader=yaml.FullLoader)
        with open("../frontend/src/brownie-config.json", "w") as brownie_config_json:
            json.dump(config_dict, brownie_config_json)


def copy_folder_to_front_end(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def main():
    update_frontend()

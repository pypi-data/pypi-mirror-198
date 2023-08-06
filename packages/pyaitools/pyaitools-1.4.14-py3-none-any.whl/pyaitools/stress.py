import os
import argparse

import sys
from importlib import util
from os.path import basename
from os.path import exists
from types import ModuleType


def load_package_from_path(pkg_path: str, config_name) -> ModuleType:
    init_path = f"{pkg_path}/__init__.py"
    if not os.path.exists(init_path):
        with open(init_path, "w") as fp:
            fp.write("")
    name = basename(config_name)

    spec = util.spec_from_file_location(name, init_path)
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    return module


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument(
        "--uri", "-u", required=True, help="本地浏览器打开地址", default="http://0.0.0.0:80"
    )
    parser.add_argument("--config", "-c", required=True, help="压测服务的配置文件名")
    args = parser.parse_args()
    uri = args.uri
    uri_port = uri.replace("http://", "").replace("https://", "").split(":")
    config = args.config
    path = os.getcwd()
    import sys

    sys.path.append(path)
    from stress_config import (
        url,
        request_body,
        step_time,
        step_load,
        spawn_rate,
        time_limit,
    )

    # print(url)
    root_config = os.path.abspath(__file__).replace("stress.py", "")
    with open(root_config + "/temp.py", "w") as fp:
        fp.write(f"request_body={request_body}\n")
        fp.write(f"step_time={step_time}\n")
        fp.write(f"step_load={step_load}\n")
        fp.write(f"spawn_rate={spawn_rate}\n")
        fp.write(f"time_limit={time_limit}\n")
    config_file = root_config + "/stress_locust.py"
    comm = f"locust -f {config_file} --host {url} --web-host={uri_port[0]} --web-port={uri_port[1]}"
    os.system(comm)
    os.system(f"rm {root_config+'/temp.py'}")


if __name__ == "__main__":
    main()

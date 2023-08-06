import argparse
from io import TextIOWrapper
import logging
from typing import Protocol
from base.logger import logger
import os
import yaml

__version__ = "0.1.8"


class Args(Protocol):
    registry: str
    images_dir: str
    namespace: str
    file: TextIOWrapper
    dir: str
    apps: str
    debug: bool
    dist_dir: str


def load_yaml_data(file):
    with open(file, encoding="utf-8", mode='r') as loader:
        return yaml.safe_load(loader)


def save_image(app: str, img: str, args: Args):
    os.system(f'docker pull {img}')
    if args.registry is not None:
        r = args.registry + img[img.index('/'):]
        os.system(f'docker tag {img} {r}')
        img = r

    gz_file = os.path.join(args.images_dir, f'{app}.tar.gz')
    os.system(f'docker save {img} | gzip > {gz_file}')

    img_file = f'images/{app}.tar.gz'
    args.file.write(f'docker load < {img_file}\n')
    args.file.write(f'docker push {img}\n\n')


def apply_yaml(app: str, args: Args):
    app_dir = os.path.join(args.dir, app)
    app_file = os.path.join(args.images_dir, f"{app}.yaml")
    if args.namespace is not None:
        os.system(
            f'helm template {app_dir} -n {args.namespace} > {app_file}')
    else:
        os.system(f'helm template {app_dir} > {app_file}')


def handle_app(app: str, args: Args):
    values_file = os.path.join(args.dir, app, 'values.yaml')
    if not os.path.exists(values_file):
        logger.error(f'应用不存在:{values_file}')
        return

    try:
        data = load_yaml_data(values_file)
        repository: str = data['image']['repository']
        tag: str = data['image']['tag']

        img = f'{repository}:{tag}'
        logger.info(f'处理：{img}')

        save_image(app, img, args)

        if app == 'qt-quant':
            etl_img = data['initContainers'][0]['image']
            save_image('qt-etl', etl_img, args)

        apply_yaml(app, args)

    except Exception as ex:
        logger.error(ex)
        pass


def main():
    parser = argparse.ArgumentParser(description="升级打包工具")
    parser.add_argument("-v", "--version", action="version",
                        version=__version__, help="display app version.")
    parser.add_argument("-a", "--apps", help="打包的应用清单，用逗号分隔。")
    parser.add_argument("-d", "--dir", help="应用清单charts目录")
    parser.add_argument("-r", "--registry", help="目标registry")
    parser.add_argument("-n", "--namespace", help="K8s命名空间")
    parser.add_argument("--debug", action="store_true", default=False,
                        help="启用debug模式，会输出更多信息。")

    args: Args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    args.dist_dir = 'dist'
    args.images_dir = os.path.join(args.dist_dir, 'images')

    logger.info(f'Charts目录:{args.dir}')
    logger.info(f'需要打包的应用:{args.apps}')
    if args.registry is not None:
        logger.info(f'registry={args.registry}')

    if not os.path.exists(args.dir):
        logger.error(f'目录不存在:{args.dir}')
        return

    if not os.path.exists(args.images_dir):
        os.makedirs(args.images_dir, exist_ok=True)

    file = open(os.path.join(args.dist_dir, 'upload.sh'),
                encoding='utf-8', newline='\n', mode='w')
    args.file = file
    file.write("#!/bin/bash\n")

    for app in args.apps.split(','):
        handle_app(app, args)
    file.close()


if __name__ == "__main__":
    main()

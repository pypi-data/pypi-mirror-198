import argparse
from io import TextIOWrapper
import logging
from typing import Protocol
from base.logger import logger
import os
import yaml

__version__ = "0.1.9"


class Args(Protocol):
    registry: str
    images_dir: str
    yaml_dir: str
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
    app_file = os.path.join(args.yaml_dir, f"{app}.yaml")
    if args.namespace is not None:
        os.system(
            f'helm template {app_dir} -n {args.namespace} > {app_file}')
    else:
        os.system(f'helm template {app_dir} > {app_file}')


def get_images(app: str, data: any):
    if app == 'qt-quant':
        repository: str = data['image']['repository']
        tag: str = data['image']['tag']
        etl_img = data['initContainers'][0]['image']
        return [f'{repository}:{tag}', etl_img]
    elif app == 'cp-kafka':
        r1: str = data['cp-kafka']['image']
        t1: str = data['cp-kafka']['imageTag']

        r2: str = data['cp-zookeeper']['image']
        t2: str = data['cp-zookeeper']['imageTag']
        return [f'{r1}:{t1}', f'{r2}:{t2}']
    else:
        repository: str = data['image']['repository']
        tag: str = data['image']['tag']
        return [f'{repository}:{tag}']


def handle_app(app: str, args: Args):
    values_file = os.path.join(args.dir, app, 'values.yaml')
    if not os.path.exists(values_file):
        return

    logger.info(f'处理应用{app}')
    try:
        if app in args.apps:
            data = load_yaml_data(values_file)
            images = get_images(app, data)
            for img in images:
                save_image(app, img, args)

        apply_yaml(app, args)

    except Exception as ex:
        logger.error(ex)


def make_dirs(dirs: list[str]):
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d, exist_ok=True)


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
    args.yaml_dir = os.path.join(args.dist_dir, 'yaml')
    args.apps = args.apps.split(',')

    logger.info(f'Charts目录:{args.dir}')
    logger.info(f'需要打包的应用:{args.apps}')
    if args.registry is not None:
        logger.info(f'registry={args.registry}')

    if not os.path.exists(args.dir):
        logger.error(f'Charts目录不存在:{args.dir}')
        return

    make_dirs([args.images_dir, args.yaml_dir])

    file = open(os.path.join(args.dist_dir, 'upload.sh'),
                encoding='utf-8', newline='\n', mode='w')
    args.file = file
    file.write("#!/bin/bash\n")

    for app in os.listdir(args.dir):
        handle_app(app, args)

    file.close()


if __name__ == "__main__":
    main()

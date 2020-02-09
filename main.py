from user_project.app import app
from user_project.config import DB_PATH
import argparse
import logging
import os

logging.basicConfig()
log = logging.getLogger()

parser = argparse.ArgumentParser()
parser.add_argument("--listen_port", type=int, help="bind port", default="8080")
parser.add_argument("--debug", action='store_true', help="for more verbosity")

args = parser.parse_args()

if args.debug:
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.INFO)


def main():
    if not os.path.isfile(DB_PATH):
        log.error("Database does not exist, please run init_data.py")
        exit(1)

    try:
        app.run(port=args.listen_port)
    except Exception as e:
        log.error(f"Can't start at port {args.listen_port}")


if __name__ == '__main__':
    main()

from user_project.app import app
import argparse
import logging

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
    try:
        app.run(port=args.listen_port)
    except Exception as e:
        log.error(f"Can't start at port {args.listen_port}")


if __name__ == '__main__':
    main()

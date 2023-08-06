import argparse
from base.logger import log
from program.__version__ import __version__


def main():
    parser = argparse.ArgumentParser(description="Excel报表解析程序")
    parser.add_argument("-v", "--version", action="version",
                        version=__version__, help="显示程序版本号。")
    args = parser.parse_args()

    # log.info("start")


if __name__ == '__main__':
    main()

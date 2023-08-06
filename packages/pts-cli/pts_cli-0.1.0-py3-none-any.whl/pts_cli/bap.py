import argparse
import sys


class BetterArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help()
        sys.stderr.write(f'error: {message}\n')
        sys.exit(2)

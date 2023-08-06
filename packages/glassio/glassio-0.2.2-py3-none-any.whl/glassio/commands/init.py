import os.path
import shutil
from argparse import ArgumentParser, Namespace
from glassio.command import Command


class Init(Command):

    NAME = "init"
    HELP = "initialize a new project in the current directory"

    _quiet: bool = False

    def init_argument_parser(self, parser: ArgumentParser) -> None:
        parser.add_argument("-q", "--quiet", action="store_true", default=False, help="disable progress messages")

    def setup(self, args: Namespace) -> None:
        self._quiet = args.quiet

    def process_directory(self, dir_name: str):
        curdir = os.path.abspath(os.curdir)
        for filename in os.listdir(dir_name):
            full_filename = os.path.join(dir_name, filename)
            if os.path.isdir(full_filename):
                new_dir = os.path.join(curdir, filename)
                if not self._quiet:
                    print(f"creating new directory {new_dir}")
                os.makedirs(new_dir)
                if not self._quiet:
                    print(f"jumping into {new_dir}")
                os.chdir(new_dir)
                self.process_directory(full_filename)
                if not self._quiet:
                    print(f"jumping back into {curdir}")
                os.chdir(curdir)
            else:
                new_filename = os.path.abspath(os.path.join(curdir, filename))
                if not self._quiet:
                    print(f"copying {full_filename} to {new_filename}")
                shutil.copy(full_filename, new_filename)

    def run_sync(self) -> None:

        init_command_dir = os.path.dirname(__file__)
        glasskit_dir = os.path.abspath(os.path.join(init_command_dir, ".."))
        templates_dir = os.path.join(glasskit_dir, "templates")
        if not self._quiet:
            print(f"using templates directory {templates_dir}")
        self.process_directory(templates_dir)

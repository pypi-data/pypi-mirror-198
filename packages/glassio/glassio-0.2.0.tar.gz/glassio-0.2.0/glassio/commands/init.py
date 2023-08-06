import os.path
import shutil

from glassio.command import Command


class Init(Command):

    NAME = "init"
    HELP = "initialize a new project in the current directory"

    def process_directory(self, dir_name: str):
        curdir = os.path.abspath(os.curdir)
        for filename in os.listdir(dir_name):
            full_filename = os.path.join(dir_name, filename)
            if os.path.isdir(full_filename):
                new_dir = os.path.join(os.curdir, filename)
                os.makedirs(new_dir)
                os.chdir(new_dir)
                self.process_directory(full_filename)
                os.chdir(curdir)
            else:
                new_filename = os.path.abspath(os.path.join(curdir, filename))
                shutil.copy(full_filename, new_filename)

    def run_sync(self) -> None:
        init_command_dir = os.path.dirname(__file__)
        glasskit_dir = os.path.abspath(os.path.join(init_command_dir, ".."))
        templates_dir = os.path.join(glasskit_dir, "templates")
        self.process_directory(templates_dir)

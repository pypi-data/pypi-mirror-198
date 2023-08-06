import os
import shutil


class FileUtils:
    @staticmethod
    def absPath(path):
        # this function should be the abs path relative to the project root
        basePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(basePath, path)

    @staticmethod
    def copyDir(src, dst, symlinks=False, ignore=None):
        # copy dir
        # do not use for
        shutil.copytree(src, dst, symlinks, ignore)

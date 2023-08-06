import os
import shutil


class FileUtils:
    @staticmethod
    def copyDir(src, dst, symlinks=False, ignore=None):
        # copy dir
        # do not use for
        shutil.copytree(src, dst, symlinks, ignore)

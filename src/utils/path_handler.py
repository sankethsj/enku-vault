import os
import sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        filename = relative_path.split("/")[-1]
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), relative_path)

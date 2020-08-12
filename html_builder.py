"""
html_builder
Final Project
Author: Nhu Quynh Duong
"""
from wizard_mode import get_user_input
from website_mode import get_user_input
import sys


def wizard_main():
    """
    Runs the wizard mode
    :return: None
    """
    get_user_input()


def website_main():
    """
    Runs the website_mode
    :return: None
    """
    get_user_input()


def main():
    """
    Runs the whole program
    :return: None
    """
    if len(sys.argv) == 0:
        wizard_main()
    else:
        website_main()


if __name__ == '__main__':
    main()

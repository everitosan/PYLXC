"""
This module enable arguments for the tool
"""

import argparse


def parse():
    parser = argparse.ArgumentParser(
        description="Parse arguments to export or create")
    parser.add_argument(
        "-e",
        "--export",
        type=str,
        required=False
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        required=False
    )

    parser.add_argument(
        "-f",
        "--file",
        type=str,
        required=False
    )

    return parser.parse_args()

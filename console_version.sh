#!/bin/bash
cd $(dirname "$0")

~/wkc-env/venv/bin/python3 console_version.py "$@"

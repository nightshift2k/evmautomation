#!/usr/bin/env bash

set -ex

python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 -m pip install -e .
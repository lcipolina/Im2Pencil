#!/bin/sh

(cd pretrained_models; bash download_models.sh)

python3 batch_fixer.py

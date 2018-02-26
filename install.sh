#!/bin/bash

set ENV_NAME = dicom_env
virtualenv $ENV_NAME
pip install -r requirements.txt
python -m ipykernel install --user --name=$ENV_NAME
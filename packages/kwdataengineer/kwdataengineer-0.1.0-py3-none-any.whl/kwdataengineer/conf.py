# -*- coding: utf-8 -*-
import os


PROJECT_NAME = 'KiwoomDataEngineer'
DATABASE_NAME = 'Kiwoom'
PACKAGE_NAME = 'kwdataengineer'

# 운영체제에 따라 달라진다
PYPJTS_PATH = 'C:\pypjts'
PROJECT_PATH = os.path.join(PYPJTS_PATH, PROJECT_NAME)
DATA_PATH = os.path.join(PYPJTS_PATH, PROJECT_NAME, 'pkgs', PACKAGE_NAME, 'Data')
SCHEMA_FILE_PATH = os.path.join(DATA_PATH, 'SchemaCSV')
DEV_GUIDE_PATH = os.path.join(DATA_PATH, 'ModelDataText')
DOCS_PATH = os.path.join(DATA_PATH, 'Docs')

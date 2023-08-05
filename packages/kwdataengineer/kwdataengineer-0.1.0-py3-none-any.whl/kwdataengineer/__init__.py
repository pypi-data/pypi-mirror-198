# -*- coding: utf-8 -*-
from dataengineer.conf import Database, ProjectInfo
from kwdataengineer import conf
Database.set('name', conf.DATABASE_NAME)
ProjectInfo.set('ProjectName', conf.PROJECT_NAME)

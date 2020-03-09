# -*- coding: utf-8 -*-
#コーディング: utf-8
#------------------------------------------------------------------------------
import os
import sys
import datetime
from collections import OrderedDict
#------------------------------------------------------------------------------
def _sphinxDict():
    _dict=OrderedDict()

    #sourceの上のフォルダ名
    _dict["project"]=project = os.path.dirname(os.path.abspath(__file__)).split("\\")[-2]

    _user=os.environ["USERNAME"]
    _dict["copyright"]="%s : %s (%s@toei-anim.co.jp)" % (datetime.date.today().year,_user,_user)

    _dict["version"]='0.0.1'
    _dict["release"]='0.0.1'

    return _dict

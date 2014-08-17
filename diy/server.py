#!/usr/bin/env python
import os
import sys

cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, cwd)

import app

app.main(os.environ['OPENSHIFT_DIY_IP'], os.environ['OPENSHIFT_DIY_PORT'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

m = re.search('[0-9]','abcd4f')
print(m.group(0))

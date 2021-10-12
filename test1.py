# -*- coding: utf-8 -*-

import re

# s1 = "Boeing has unveiled its newest line of business jets, which the company says will allow VIP travelers to fly nonstop between any two cities on Earth."

s1 = "Boeing is a USA company. USA has many giant companies, including Boeing"

print(re.findall('Boeing$', s1))


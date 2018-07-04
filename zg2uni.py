# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input

    output = output.replace(u'\u106A', u'\u1009')
    output = output.replace(u'\u103D', u'\u103E') #ha
    output = output.replace(u'\u103C', u'\u103D') #wa
    output = output.replace(u'\u1033', u'\u102F') #ta
    output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]', u'\u103C', output)#ya
    output = output.replace('u\u103A', u'\u103B') #ra
    output = output.replace('u\u1039', u'\u103A') #nghtet
    output = output.replace('u\u106B', u'\u100A') #nya
    output = re.sub(u'\u107B', u'\u1039\u1018', output)#basint
    output = re.sub(u'\u1062', u'\u1039\u1002', output)#gasint
    output = re.sub(u'\u1071', u'\u1039\u1010', output)#tasint
    output = re.sub(u'(\u103C)([\u1000-\u1020])', u'\\2\\1', output)
    output = re.sub(u'\u1031([\u1000-\u1021])', u'\\1\u1031', output)
    output = re.sub(u'\u1031([\u103B-\u103E\+])', u'\\1\u1031', output)

    return output

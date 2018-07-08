# -*- coding: utf-8 -*-
import re


def replace(input):
    # replace each zawgyi code point with equivalent code point in unicode
    output = input

    output = output.replace(u'\u103A', u'\u1039') # athet
    output = re.sub(u'\u103B', u'\u103A', output) # yapint
    output = re.sub(u'\u103C', u'\u103B', output) # yayit
    output = re.sub(u'\u103D', u'\u103C', output) # waswe
    output = re.sub(u'\u103E', u'\u103D', output) # hahto
    output = re.sub(u'\u103F', u'\u1086', output) # thagyi

    return output


def precompose(input):
    output = input

    output = re.sub(u'\u1064')


def convert(input):
    output = input

    output = replace(output)

    return output

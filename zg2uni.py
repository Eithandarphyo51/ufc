# -*- coding: utf-8 -*-
import re


def replace(input):
    # replace each zawgyi code point with equivalent code point in unicode
    output = input

    
    output = output.replace(u'\u106A', u'\u1009') #nyalay
    output = re.sub(u'\u1025(?=[\u103A\u102C])', u'\u1009', output) #nyalay yaychar
    output = re.sub(u'\u106B', u'\u100A', output) #nya
    output = re.sub(u'\u1090', u'\u101B', output) #yagaut
    output = re.sub(u'\u1033', u'\u102F', output) #tachaung
    output = re.sub(u'\u1034', u'\u1030', output) #hnachaung
    output = re.sub(u'[\u103D\u1087]', u'\u103E', output) #ha
    output = re.sub(u'\u103C', u'\u103D', output) #wa
    output = re.sub(u'\u1086', u'\u103F', output) #thagyi
    output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]', u'\u103C', output)#yayit
    output = re.sub(u'[\u103A\u107D]', u'\u103B', output) #rapint
    output = re.sub(u'\u1039', u'\u103A', output) #athet
    output = re.sub(u'\u104E', u'\u104E\u1044\u103A\u1038', output) #lagaung
    output = re.sub(u'[\u1037\u1094\u1095]', u'\u1037', output) #autkamyint
    output = re.sub(u'\u108F', u'\u1014', output) #nange


    return output


def decompose(input):
    #decomposed combined characters to sequenced characters
    output = input

    #ngasint
    output = re.sub(u'([u1000-u1021])\u1064', u'\u1064\\1', output)
    output = re.sub(u'([u1000-u1021])\u108B', u'\u1064\\1\u102D', output)
    output = re.sub(u'([u1000-u1021])\u108c', u'\u1064\\1\u102E', output)
    output = re.sub(u'([u1000-u1021])\u108D', u'\u1064\\1\u1036', output)
    output = re.sub(u'\u108E', u'\u102D\u1036', output)
    output = re.sub(u'\u1064', u'\u1004\u103A\u1039', output)

    output = re.sub(u'\u108A', u'\u103D\u103E', output)  #wahahto
    output = re.sub(u'\u1088', u'\u103E\u102F', output)  # hahto_tachaung
    output = re.sub(u'\u1089', u'\u103E\u1030', output)  # hatho_hnachaung
    output = re.sub(u'\u105A', u'\u102B\u103A', output)  # yaycharshathto

    #patsint
    output = re.sub(u'\u1060', u'\u1039\u1000', output)#kasint
    output = re.sub(u'\u1061', u'\u1039\u1001', output)#khasint
    output = re.sub(u'\u1062', u'\u1039\u1002', output)#gasint
    output = re.sub(u'\u1063', u'\u1039\u1003', output)#gagyisint
    output = re.sub(u'\u1065', u'\u1039\u1005', output)#sasint
    output = re.sub(u'\u1066\u1067', u'\u1039\u1006', output)#salainsint
    output = re.sub(u'\u1068', u'\u1039\u1007', output)#zasint
    output = re.sub(u'\u1069', u'\u1039\u1008', output)#zamyinzwesint
    output = re.sub(u'\u106C', u'\u1039\u100B', output)#tatasint
    output = re.sub(u'\u106D', u'\u1039\u100C', output)#htatwinsint
    output = re.sub(u'\u1070', u'\u1039\u100F', output)#nagyisint
    output = re.sub(u'\u1071\u1072', u'\u1039\u1010', output)#tasint
    output = re.sub(u'\u1073\u1074', u'\u1039\u1011', output)#htasint
    output = re.sub(u'\u1075', u'\u1039\u1012', output)#dasint
    output = re.sub(u'\u1076', u'\u1039\u1013', output)#dachintsint
    output = re.sub(u'\u1077', u'\u1039\u1014', output)#nasint
    output = re.sub(u'\u1078', u'\u1039\u1015', output)#pasint
    output = re.sub(u'\u1079', u'\u1039\u1016', output)#phasint
    output = re.sub(u'\u107A', u'\u1039\u1017', output)#bachintsint
    output = re.sub(u'\u107B', u'\u1039\u1018', output)#basint
    output = re.sub(u'\u107C', u'\u1039\u1019', output)#masint
    output = re.sub(u'\u1085', u'\u1039\u101C', output)#lasint
    output = re.sub(u'\u106E', u'\u100D\u1039\u100D', output)#tata-2lonesint
    output = re.sub(u'\u106F', u'\u100E\u1039\u100D', output)#dayin_tasint
    output = re.sub(u'\u1091', u'\u100F\u1039\u100D', output)#nagyi_dayinkaut_sint
    output = re.sub(u'\u1092', u'\u100B\u1039\u100C', output)
    output = re.sub(u'\u1097', u'\u100B\u1039\u100B', output)

    return output

def visual2logical(input):

    output = input
    # reorder yayit to CMV format
    output = re.sub(u'(\u103C)([\u1000-\u1021])', u'\\2\\1', output)
    # reorder thawayhtoo
    output = re.sub(u'(\u1031)([\u1000-\u1021])', u'\\1\u1031', output)
    output = re.sub(u'(\u1031)([\u103B-\u103E\+])', u'\\1\u1031', output)
    output = re.sub(u'(\u102F)(\u102D\u102E])', u'\\2\\1', output)
    output = re.sub(u'(\u1030)(\u102D\u102E])', u'\\2\\1', output)

    return output



def convert(input):

    output = input


    output = replace(output)
    output = decompose(output)
    output = visual2logical(output)

    return output

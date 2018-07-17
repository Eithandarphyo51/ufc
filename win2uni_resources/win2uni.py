# -*- coding: utf-8 -*-
import re

def replace(input):
    """ Replace each win char value with equivlant code point in Unicode.
    Conversions will be one on one. """
    output = input
    output = output.replace(u'\u0075', u'\u1000') #kagyi
    output = output.replace(u'\u0063', u'\u1001') #khakway
    output = output.replace(u'\u002A', u'\u1002') #gange
    output = output.replace(u'\u0043', u'\u1003') #gagyi
    output = output.replace(u'\u0069', u'\u1004') #nga
    output = output.replace(u'\u0070', u'\u1005') #salone
    output = output.replace(u'\u0071', u'\u1006') #salane
    output = output.replace(u'\u005A', u'\u1007') #zakwe
    output = output.replace(u'\u006E', u'\u100A') #nya
    output = output.replace(u'\u00F1', u'\u100A') #nya
    output = output.replace(u'\u0023', u'\u100B') #tatalingyake
    output = output.replace(u'\u0058', u'\u100C') #htawinbal
    output = output.replace(u'\u0021', u'\u100D') #dayinkauk
    output = output.replace(u'\u00A1', u'\u100E') #dayinmoke
    output = output.replace(u'\u0050', u'\u100F') #nagyi
    output = output.replace(u'\u0077', u'\u1010') #tawinpu
    output = output.replace(u'\u0078', u'\u1011') #htasinhtoo
    output = output.replace(u'\u0027', u'\u1012') #dadway
    output = output.replace(u'\u0065', u'\u1014') #nange
    output = output.replace(u'\u0079', u'\u1015') #pasaut
    output = output.replace(u'\u007A', u'\u1016') #phaoohtok
    output = output.replace(u'\u0041', u'\u1017') #bahtetchint
    output = output.replace(u'\u0062', u'\u1018') #bakone
    output = output.replace(u'\u0072', u'\u1019') #ma
    output = output.replace(u'\u002C', u'\u101A') #yapatlat
    output = output.replace(u'\u0026', u'\u101B') #yakaut
    output = output.replace(u'\u0076', u'\u101C') #la
    output = output.replace(u'\u006F', u'\u101E') #tha
    output = output.replace(u'\u005B', u'\u101F') #ha
    output = output.replace(u'\u0056', u'\u1020') #lagyi
    output = output.replace(u'\u0074', u'\u1021') #ak
    output = output.replace(u'\u00FE', u'\u1024') #ee
    output = output.replace(u'\u004F', u'\u1025') #ou
    output = output.replace(u'\u007B', u'\u1027') #a
    output = output.replace(u'\u00F3', u'\u103F') #thagyi
    output = output.replace(u'\u00DA', u'\u1009') #nyalay
    output = output.replace(u'\u00FC', u'\u104C') #hnigh
    output = output.replace(u'\u00ED', u'\u104D') #ywat
    output = output.replace(u'\u0073', u'\u103B') #yapint
    output = re.sub(u'[\u0042\u004D\u004E\u0060\u006A\u007E\u00EA]', u'\u103C', output) #yayit
    output = output.replace(u'\u0047', u'\u103D') #waswe
    output = output.replace(u'\u0053', u'\u103E') #hahto
    output = output.replace(u'\u004B', u'\u102F') #tachaung
    output = output.replace(u'\u006B', u'\u102F') #tachaung
    output = output.replace(u'\u004C', u'\u1030') #2chaung
    output = output.replace(u'\u006C', u'\u1030') #2chaung
    output = output.replace(u'\u0067', u'\u102B') #yaychar
    output = output.replace(u'\u006D', u'\u102C') #yaychar
    output = output.replace(u'\u0064', u'\u102D') #lonegyitin
    output = output.replace(u'\u0044', u'\u102E') #lonegyitinsankhat
    output = output.replace(u'\u0061', u'\u1031') #thawayhto
    output = output.replace(u'\u004A', u'\u1032') #nathtomyit
    output = output.replace(u'\u0066', u'\u103A') #athet
    output = re.sub(u'[\u0055\u0059\u0068]', u'\u1037', output) #autmyit
    output = output.replace(u'\u003B', u'\u1038') #witsapaut
    output = output.replace(u'\u0048', u'\u1036') #thaythaytin
    output = output.replace(u'\u003F', u'\u104A') #pokekalay
    output = output.replace(u'\u002F', u'\u104B') #pokema
        
    
    output = output.replace(u'\u0030', u'\u1040') #0
    output = output.replace(u'\u0031', u'\u1041') #1
    output = output.replace(u'\u0032', u'\u1042') #2
    output = output.replace(u'\u0033', u'\u1043') #3
    output = output.replace(u'\u0034', u'\u1044') #4
    output = output.replace(u'\u0035', u'\u1045') #5
    output = output.replace(u'\u0036', u'\u1046') #6
    output = output.replace(u'\u0037', u'\u1047') #7
    output = output.replace(u'\u0038', u'\u1048') #8
    output = output.replace(u'\u0039', u'\u1049') #9

    return output


def decompose(input):
    # decomposed combined characters to sequenced characters

    output = input

    output = re.sub(u'\u003a', u'\u102b\u103a', output)  # yaycharshaehtoe
    output = re.sub(u'[\u003c\u003e]', u'\u103c\u103d', output)  # yayitwaswe
    output = re.sub(u'\u0040', u'\u100f\u1039\u100d', output)  # nagyihtawenbaesint
    output = re.sub(u'\u0049', u'\u103e\u102f', output)  # hatoe1chaungngin
    output = re.sub(u'\u0052', u'\u103b\u103d', output)  # yapintwaswe
    output = re.sub(u'\u0054', u'\u103d\u103e', output)  # waswehatoe
    output = re.sub(u'\u0057', u'\u103b\u103d\u103e', output)  # yapintwaswehatoe

    # patsint
    output = re.sub(u'\u00FA', u'\u1039\u1000', output)  # kasint
    output = re.sub(u'\u00A9', u'\u1039\u1001', output)  # khasint
    output = re.sub(u'\u00BE', u'\u1039\u1002', output)  # gasint
    output = re.sub(u'\u00A2', u'\u1039\u1003', output)  # gagyisint
    output = re.sub(u'\u00F6', u'\u1039\u1005', output)  # sasint
    output = re.sub(u'\u00E4', u'\u1039\u1006', output)  # salainsint
    output = re.sub(u'\u00D1', u'\u1039\u1008', output)  # zamyinzwesint
    output = re.sub(u'\u00B3', u'\u1039\u100B', output)  # tatalingyakesint
    output = re.sub(u'\u00B2', u'\u1039\u100C', output)  # htatwinbaesint
    output = re.sub(u'\u00D6', u'\u1039\u100F', output)  # nagyisint
    output = re.sub(u'\u00C5', u'\u1039\u1010', output)  # tasint
    output = re.sub(u'\u00AC', u'\u1039\u1011', output)  # htasint
    output = re.sub(u'\u00B4', u'\u1039\u1012', output)  # dasint
    output = re.sub(u'\u00A8', u'\u1039\u1013', output)  # daautchintsint
    output = re.sub(u'\u00E9', u'\u1039\u1014', output)  # nasint
    output = re.sub(u'\u00DC', u'\u1039\u1015', output)  # pasint
    output = re.sub(u'\u00E6', u'\u1039\u1016', output)  # phasint
    output = re.sub(u'\u00C1', u'\u1039\u1017', output)  # bahtetchintsint
    output = re.sub(u'\u00C7', u'\u1039\u1018', output)  # bakonesint
    output = re.sub(u'\u00AE', u'\u1039\u1019', output)  # masint
    output = re.sub(u'\u2019', u'\u1039\u101C', output)  # lasint
    output = re.sub(u'\u00D7', u'\u100D\u1039\u100D', output)  # tata-2lonesint

    return output

def visual2logical(input):
    # reorder the sequence of characters from visual to logical
    output = input

    #reorder yayit to CMV format
    output = re.sub(u'(\u103C)([\u1000-\u1020])', u'\\2\\1', output)

    # reorder thawayhtoo
    output = re.sub(u'\u1031([\u1000-\u1021])', u'\\1\u1031', output)
    output = re.sub(u'\u1031([\u103B-\u103E\+])', u'\\1\u1031', output)

    return output


def convert(input):
    
    output = replace(input)
    output = decompose(output)
    output = visual2logical(output)
        
    return output

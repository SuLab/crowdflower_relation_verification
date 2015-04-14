# last updated 2015-02-24 Tong Shu Li
import unicodedata

def convert_unicode_to_ascii(text):
#   removes mostly non-breaking spaces
    text = unicodedata.normalize("NFKD", text)

    text = text.replace(u'\xb1', "+/-") # replace the plus minus symbol
    text = text.replace(u'\xb7', ".") # replace middle dot with period (pmid 20491765)

    text = text.replace(u'\u03b1', "alpha")
    text = text.replace(u'\u03b2', "beta")
#   replace mu with micro (pmid 24626782, sid 155628315)
#   sometimes called "mu" instead of micro... what to do????
    text = text.replace(u'\u03bc', "micro")
#   replace sigma with sigma (pmid 24474250, sid 153797529)
    text = text.replace(u'\u03c3', "sigma")

    text = text.replace(u'\u0308', "") # delete the two dots on top
    text = text.replace(u'\u0301', "") # delete accent
    text = text.replace(u'\u2264', "</=") # less than equal to pmid 24416322
    text = text.replace(u'\u2265', ">/=") # pmid 22457394

    text = text.replace(u'\u0394', "Delta") # pmid 23993575
    text = text.replace(u'\u03b4', "delta")
    text = text.replace(u'\u03c7', "chi") # pmid 21888663
    text = text.replace(u'\u03c1', "rho")
    text = text.replace(u'\u03ba', "kappa") # pmid 22694930
    text = text.replace(u'\u03b3', "gamma") # pmid 22303015
    text = text.replace(u'\u03b5', "epsilon")
    text = text.replace(u'\u03b6', "zeta")

    text = text.replace(u'\xd7', "x") # pmid 22694930

    text = text.replace(u'\xae', "(R)")
    text = text.replace(u'\xa9', "(c)")
    text = text.replace(u'\u2192', "->")
    text = text.replace(u'\u2019', "'")
    text = text.replace(u'\u2213', "-/+")
    text = text.replace(u'\u0327', "")

    return text.encode("ascii")

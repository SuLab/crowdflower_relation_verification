# last updated 2015-04-09 toby
"""
Grabs annotations about the same two concepts as the current
annotation. It is likely the other annotations did not make
it into the final version of the EU-ADR.
"""
import re

import sys
sys.path.append("/home/toby/global_util/")
from file_util import read_file

def correct_format(raw_id):
    return re.match(r'^t_\d{8}_rel_\d+$', raw_id) is not None

# given a raw id, get the original row of data
def get_orig_annotation(raw_id):
    assert correct_format(raw_id)

    pmid = raw_id[2:10]
    fname = "id_{0}.txt".format(pmid)

    loc = "/home/toby/crowdsourcing/id_raw_euadr_corpus"

    for line in read_file(fname, loc):
        vals = line.split("\t")
        if len(vals) == 12 and vals[11] == raw_id:
            return vals

def get_all_raw_annotations(pmid):
    fname = "id_{0}.txt".format(pmid)
    loc = "/home/toby/crowdsourcing/id_raw_euadr_corpus"

    ans = []
    for line in read_file(fname, loc):
        vals = line.split("\t")
        if len(vals) == 12:
            ans.append(vals)

    return ans

def retrieve_similar_annotations(raw_id):
    """
    Grabs the annotations which were about the same two concepts as the given id
    """
    main_annotation = get_orig_annotation(raw_id)

    sub = main_annotation[3]
    obj = main_annotation[4]

    pmid = raw_id[2:10]
    all_annotations = get_all_raw_annotations(pmid)

    ans = []
    for annotation in all_annotations:
        if sub == annotation[3] and obj == annotation[4]:
            ans.append(annotation)

    return ans

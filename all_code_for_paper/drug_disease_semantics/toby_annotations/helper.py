# last updated 2015-04-05 toby
import pandas as pd
import subprocess

import sys
sys.path.append("/home/toby/global_util/")
from file_util import exists

sys.path.append("/home/toby/crowdsourcing/drug_disease_semantics/src/")
from filter_data import filter_data

def color(text, color):
    ans = "92" if color == "green" else "94"
    return "\033[{0}m{1}\033[0m".format(ans, text)

def highlight_concepts(text, sub_text, obj_text):
    if text == sub_text: # disease
        return color(text, "blue")

    if text == obj_text: # drug
        return color(text, "green")

    return text

def highlight_sentence(row):
    positions = sorted([0, len(row["original_sentence"]),
        row["subject_start"], row["subject_end"],
        row["object_start"], row["object_end"]])

    sentence = row["original_sentence"]

    temp = []
    for i in range(len(positions) - 1):
        temp += highlight_concepts(sentence[positions[i] : positions[i+1]],
            row["subject_text"], row["object_text"])

    return "".join(temp)

def wait():
    print "Press enter to continue"
    a = raw_input()
    return

def get_input(prompt, poss_answers):
    while True:
        print prompt
        print "Your choices are: {0}".format(poss_answers)
        response = raw_input()

        if response in poss_answers:
            print "Commit input with \"{0}\"? y/n".format(response)
            ans = raw_input()
            if ans == "y":
                return response
        else:
            print "Answer was not acceptable. Please try again"

def work():
    """
    Get human annotations for work units.
    """
#   grab data and color the sentences for output
    settings = {
        "loc": "/home/toby/crowdsourcing/drug_disease_semantics/data",
        "fname": "job_710587_full_with_untrusted.tsv",
        "data_subset": "normal",
        "min_accuracy": 0.7,
        "max_accuracy": 1.0,
        "sentence_type": "all"
    }

    raw_data = filter_data(settings)
    sentences = raw_data.apply(highlight_sentence, axis = 1)

    raw_data["color_sentence"] = sentences # append to data frame


    print "Data read successfully. Sentences colorized"
#-----------------------------------
#   show info to annotator and get their judgement about the problem

    i = 1
    header = ["unit_id", "toby_broad_reltype", "toby_deep_sem"]
    with open("toby_annotations.txt", "a") as out:
        out.write("{0}\n".format("\t".join(header)))
        for unit_id, group in raw_data.groupby("_unit_id"):
            print "Work unit {0} of {1}".format(i, len(raw_data["_unit_id"].unique()))
            print "Unit id:", unit_id
            print
            print group.iloc[0]["color_sentence"]
            print

            prompt = "Enter broad semantic relationship:"
            choices = ["positive", "speculative", "negative", "false"]

            broad_reltype = get_input(prompt, choices)

            deep_sem = "empty"

            if broad_reltype in ["positive", "speculative"]:
                prompt = "Enter deep semantics:"
                choices = ["used_to_treat", "may_cause", "other", "no_further_info"]
                deep_sem = get_input(prompt, choices)

            out.write("{0}\t{1}\t{2}\n".format(unit_id, broad_reltype, deep_sem))
            print "Answers successfully recorded"
            print


            wait()
            subprocess.call(["clear"])


            i += 1




def main():
    name = "toby"
    print "Annotator name:", name

    ans_fname = "{0}_annotations.txt".format(name)

    if exists(ans_fname):
        print "Annotations already exist! Aborting"
        return

#---------------------------
    print "Starting to annotate..."
    work()

if __name__ == "__main__":
    subprocess.call(["clear"])
    main()
    print "Done"

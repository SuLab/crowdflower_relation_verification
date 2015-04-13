# last updated 2015-04-04 toby
import pandas as pd
import os

def filter_data(settings):
    """
    Filters raw CrowdFlower output down to data we care about.
    """
    categories = settings["categories"]
    def convert(value):
        """
        Merges each of the given categories into one.

        Ex: categories = [["positive, "speculative"], ["negative", "false"]]
        Would take 4 categories and give 2 back.
        """
        for group in categories:
            if value in group:
                return "_".join(group)

        raise Exception("wrong groups given")

    data = pd.read_csv(os.path.join(settings["loc"], settings["fname"]), sep = "\t")

    if settings["data_subset"] == "gold":
        data = data.query("_golden")
    elif settings["data_subset"] == "normal":
        data = data.query("~_golden")

    # title or regular abstract
    if settings["sentence_type"] == "title":
        data = data.query("num_sentence == 0")
    elif settings["sentence_type"] == "normal":
        data = data.query("num_sentence > 0")

    data = (data.query("{0} <= _trust <= {1}".
        format(settings["min_accuracy"], settings["max_accuracy"])))


#   combine the different categories together if necessary
    data.loc[:, "broad_rel_type"] = data["broad_rel_type"].map(convert)
    data.loc[:, "gold_std_association_type"] = data["gold_std_association_type"].map(convert)

    data = data.query("_unit_id != 698758009") # remove the cocaine test question

    return data

# last updated 2015-04-13 Tong Shu Li
import os
import pandas as pd

from check_settings import has_proper_settings

def filter_data(settings):
    """
    Filters the CrowdFlower output data down to the set that
    we care about.
    """
    def convert(value):
        """
        Merges each of the given categories into one.

        Ex: categories = [["positive, "speculative"], ["negative", "false"]]
        Would take 4 categories and give 2 back.
        """
        for group in settings["categories"]:
            if value in group:
                return "_".join(group)

    assert has_proper_settings(settings), "Incorrect settings provided!"

    data = pd.read_csv(os.path.join(settings["loc"], settings["fname"]), sep = "\t")

    if settings["data_subset"] == "gold":
        data = data.query("_golden")
    elif settings["data_subset"] == "normal":
        data = data.query("~_golden")

#       one test question was turned off halfway through
#       so we want to exclude this question in the normal data set
        data = data.query("_unit_id != 698758009")

    data = (data.query("{0} <= _trust <= {1}".
        format(settings["min_accuracy"], settings["max_accuracy"])))

#   combine the different categories together if necessary
    data.loc[:, "broad_rel_type"] = data["broad_rel_type"].map(convert)
    data.loc[:, "gold_std_association_type"] = data["gold_std_association_type"].map(convert)

    return data

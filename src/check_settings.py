# last updated 2015-04-13 Tong Shu Li
import os

def has_proper_settings(settings):
    """
    Settings:
        1. data_subset: ["gold", "normal", "all"]
            Differentiates between test questions and regular work.
        2. min_accuracy and max_accuracy: reals from 0 to 1
            Workers with trust scores outside this range are excluded.
        3. loc: a file path of the file we want to read
        4. fname: the name of the file we are trying to read
        5. categories: a list of lists specifying how to merge the
            four original relationship categories.
            [["positive", "speculative"], ["false"], ["negative"]]
            would merge positive and speculative into one choice
            while leaving false and negative alone.
    """

    assert "loc" in settings, "No directory specified"
    assert "fname" in settings, "No file name specified"

    assert os.path.exists(os.path.join(settings["loc"], settings["fname"])), "File does not exist"

    assert "data_subset" in settings, "No data subset specified"
    assert settings["data_subset"] in {"all", "gold", "normal"}, "Data subset is not a valid choice"

    assert "min_accuracy" in settings, "No minimum accuracy specified"
    assert 0 <= settings["min_accuracy"] <= 1, "Minimum accuracy is out of bounds"

    assert "max_accuracy" in settings, "No maximum accuracy specified"
    assert 0 <= settings["max_accuracy"] <= 1, "Maximum accuracy is out of bounds"

    assert settings["min_accuracy"] <= settings["max_accuracy"], "Minimum accuracy is not less than maximum accuracy"

    return True

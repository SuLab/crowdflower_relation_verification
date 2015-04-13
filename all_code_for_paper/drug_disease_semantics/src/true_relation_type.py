# last updated 2015-04-04 toby
from filter_data import filter_data

def get_euadr_relation_type(settings):
    """
    Returns the EU-ADR answer for the semantic relationship
    type for all work units.
    """
#    settings = {
#        "loc": "/home/toby/crowdsourcing/drug_disease_semantics/data",
#        "fname": "job_710587_full_with_untrusted.tsv",
#        "data_subset": "all",
#        "min_accuracy": 0.0,
#        "max_accuracy": 1.0,
#        "sentence_type": "all"
#    }

    all_data = filter_data(settings)

    euadr_relation_type = dict()
    for unit_id, group in all_data.groupby("_unit_id"):
        assert len(group["gold_std_association_type"].unique()) == 1
        euadr_relation_type[unit_id] = group["gold_std_association_type"].iloc[0]

    return euadr_relation_type

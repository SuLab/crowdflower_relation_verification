# last updated 2015-04-08 toby
import pandas as pd

def aggregate_votes(column_name, data_frame):
    """
    Given all of the human responses for one work unit,
    aggregates the results based on the column you give it.

    For each possible choice, it calculates:
        1. Total number of votes
        2. Confidence score

    Returns an unsorted data frame of the results.

    Confidence score is the sum of the trust score of
    individual workers.
    """
    temp = []
    for value, group in data_frame.groupby(column_name):
        conf_score = sum(group["_trust"])
        num_votes = len(group)

        temp.append([value, conf_score, num_votes])

    return pd.DataFrame(temp, columns = [column_name, "conf_score", "num_votes"])

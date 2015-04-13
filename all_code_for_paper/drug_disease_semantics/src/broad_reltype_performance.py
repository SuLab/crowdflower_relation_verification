# last updated 2015-04-04 toby
import pandas as pd
from aggregate_votes import aggregate_votes

def determine_broad_reltype_results(true_relation_type, data):
    """
    Calculates the agreement percentage and determines whether the
    top crowd response matches the gold standard for all work units.
    """
    result = []
    for unit_id, group in data.groupby("_unit_id"):
        ans = aggregate_votes("broad_rel_type", group)

        total_vote_score = sum(ans["conf_score"])
        percent_agreement = ans["conf_score"] / total_vote_score
        match = map(int, ans["broad_rel_type"] == true_relation_type[unit_id])

        ans.insert(len(ans.columns), "percent_agreement", percent_agreement)
        ans.insert(len(ans.columns), "match", match)
        ans.insert(0, "unit_id", unit_id)

        ans = ans.sort(["conf_score"], ascending = False)

        result.append(ans)

    return pd.concat(result)

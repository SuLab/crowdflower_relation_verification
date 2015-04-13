def get_orig_problem(data):
    result = dict()
    for unit_id, group in data.groupby("_unit_id"):
        assert len(group["original_sentence"].unique()) == 1
        assert len(group["subject_text"].unique()) == 1
        assert len(group["object_text"].unique()) == 1

        sentence = group["original_sentence"].iloc[0]
        sub_text = group["subject_text"].iloc[0]
        obj_text = group["object_text"].iloc[0]

        form_sent = sentence.replace(sub_text, "[[{0}]]".format(sub_text))
        form_sent = form_sent.replace(obj_text, "[[{0}]]".format(obj_text))

        result[unit_id] = (sub_text, obj_text, sentence, form_sent)

    return result

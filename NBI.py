from spacy.matcher import DependencyMatcher
from spacy import displacy
from not_because_dependency_patterns import not_because_dependency_patterns
import en_core_web_trf

nlp = en_core_web_trf.load(exclude=["lemmatizer"])
print("INFO: spaCy initialized successfully.")

# not <neg VERB >mark because
neg_anchorVerb_markBec = [
    # anchor token: some verb (anchor_verb)
    {"RIGHT_ID": "anchor_verb", "RIGHT_ATTRS": {"POS": "VERB"}},
    # verb > neg: anchor_verb is the right parent of a negation
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    # verb >mark "because": anchor_verb is the left parent of "because", "because" is a marker for anchor_verb
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">++",
        "RIGHT_ID": "because",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "mark"},
    },
]

# not <neg VERB >prep because
neg_anchorVerb_prepBec = [
    # anchor token: some verb (anchor_verb)
    {"RIGHT_ID": "anchor_verb", "RIGHT_ATTRS": {"POS": "VERB"}},
    # verb > neg: anchor_verb is the right parent of a negation
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    # verb >prep "because": anchor_verb is the left parent of "because", "because" is a preposition for anchor_verb
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">++",
        "RIGHT_ID": "because",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "prep"},
    },
]

# not <neg VERB >advcl VERB >mark because
neg_anchorVerb_advcl_markBec = [
    # anchor token: some verb to be anchor_verb
    {"RIGHT_ID": "anchor_verb", "RIGHT_ATTRS": {"POS": "VERB"}},
    # anchor_verb > neg: anchor_verb is the immediate head and right parent of a negation
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    # anchor_verb > advcl_child_verb: advcl_child_verb is the adverbial clause modifier and child of anchor_verb
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "advcl_child_verb",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    # advcl_child_verb > "because": "because" is a marker for and left child of advcl_child_verb
    {
        "LEFT_ID": "advcl_child_verb",
        "REL_OP": ">--",
        "RIGHT_ID": "because",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "mark"},
    },
]

# not <neg VERB >ccomp >advcl VERB >mark because
neg_anchorVerb_ccomp_advcl_markBec = [
    # anchor token: some verb to be anchor_verb
    {"RIGHT_ID": "anchor_verb", "RIGHT_ATTRS": {"POS": "VERB"}},
    # anchor_verb > neg: anchor_verb is the immediate head and right parent of a negation
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    # anchor_verb > ccomp_child_aux: ccomp_child_aux is the clausal complement and child of anchor_verb
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "ccomp_child_aux",
        "RIGHT_ATTRS": {"DEP": "ccomp"},
    },
    # ccomp_child_aux > advcl_child_verb: advcl_child_verb is the adverbial clause modifier and child of ccomp_child_aux
    {
        "LEFT_ID": "ccomp_child_aux",
        "REL_OP": ">",
        "RIGHT_ID": "advcl_child_verb",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    # advcl_child_verb > "because": "because" is a marker for and  child of advcl_child_verb
    {
        "LEFT_ID": "advcl_child_verb",
        "REL_OP": ">",
        "RIGHT_ID": "because",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "mark"},
    },
]

# not <neg VERB >advcl >ccomp VERB >mark because
neg_anchorVerb_advcl_ccomp_markBec = [
    # anchor token: some verb to be anchor_verb
    {"RIGHT_ID": "anchor_verb", "RIGHT_ATTRS": {"POS": "VERB"}},
    # anchor_verb > neg: anchor_verb is the immediate head and right parent of a negation
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    # anchor_verb > advcl_child_verb: advcl_child_verb is the adverbial clause modifier and child of anchor_verb
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "advcl_child_verb",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    # advcl_child_verb > ccomp_child_aux: ccomp_child_aux is the clausal complement and child of advcl_child_verb
    {
        "LEFT_ID": "advcl_child_verb",
        "REL_OP": ">",
        "RIGHT_ID": "ccomp_child_aux",
        "RIGHT_ATTRS": {"DEP": "ccomp"},
    },
    # ccomp_child_aux > "because": "because" is a marker for and child of ccomp_child_aux
    {
        "LEFT_ID": "ccomp_child_aux",
        "REL_OP": ">",
        "RIGHT_ID": "because",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "mark"},
    },
]

# not <neg <ccomp VERB >advcl VERB >mark because
neg_ccomp_anchorVerb_advcl_markBec = [
    {"RIGHT_ID": "anchor_verb", "RIGHT_ATTRS": {"POS": "VERB"}},
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "ccomp_child_aux",
        "RIGHT_ATTRS": {"DEP": "ccomp"},
    },
    {
        "LEFT_ID": "ccomp_child_aux",
        "REL_OP": ">",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "advcl_child_verb",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    {
        "LEFT_ID": "advcl_child_verb",
        "REL_OP": ">",
        "RIGHT_ID": "because",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "mark"},
    },
]

# not <neg VERB >prep >prep because
neg_anchorVerb_prep_prepBec = [
    {"RIGHT_ID": "anchor_verb", "RIGHT_ATTRS": {"POS": "VERB"}},
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    {
        "LEFT_ID": "anchor_verb",
        "REL_OP": ">",
        "RIGHT_ID": "prep1",
        "RIGHT_ATTRS": {"DEP": "prep"},
    },
    {
        "LEFT_ID": "prep1",
        "REL_OP": ">",
        "RIGHT_ID": "prep2",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "prep"},
    },
]

# not <neg AUX >mark because
neg_anchorAux_markBec = [
    {"RIGHT_ID": "anchor_aux", "RIGHT_ATTRS": {"POS": "AUX"}},
    {
        "LEFT_ID": "anchor_aux",
        "REL_OP": ">--",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    {
        "LEFT_ID": "anchor_aux",
        "REL_OP": ">",
        "RIGHT_ID": "because",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "mark"},
    },
]

# not <neg AUX >prep because
neg_anchorAux_prepBec = [
    {"RIGHT_ID": "anchor_aux", "RIGHT_ATTRS": {"POS": "AUX"}},
    {
        "LEFT_ID": "anchor_aux",
        "REL_OP": ">--",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    {
        "LEFT_ID": "anchor_aux",
        "REL_OP": ">++",
        "RIGHT_ID": "because",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "prep"},
    },
]

# not <neg AUX >advcl AUX >mark because
neg_anchorAux_advcl_markBec = [
    {"RIGHT_ID": "anchor_aux", "RIGHT_ATTRS": {"POS": "AUX"}},
    {
        "LEFT_ID": "anchor_aux",
        "REL_OP": ">",
        "RIGHT_ID": "negation_particle",
        "RIGHT_ATTRS": {"DEP": "neg"},
    },
    {
        "LEFT_ID": "anchor_aux",
        "REL_OP": ">++",
        "RIGHT_ID": "advcl_child_aux",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    {
        "LEFT_ID": "advcl_child_aux",
        "REL_OP": ">--",
        "RIGHT_ID": "because",
        "RIGHT_ATTRS": {"ORTH": "because", "DEP": "mark"},
    },
]

"Initialize Dependency Matcher"
dependency_matcher = DependencyMatcher(nlp.vocab)
dependency_matcher.add("find patterns", not_because_dependency_patterns)
print("INFO: dependency_matcher initialized successfully.")


def spaCy_parser(sentence):
    doc = nlp(sentence)

    doc_attr = {
        "text": [],
        "lemma": [],
        "pos": [],
        "tag": [],
        "dep": [],
        "shape": [],
        "alpha": [],
        "stop": [],
    }

    for token in doc:
        doc_attr["text"].append(token.text)
        doc_attr["lemma"].append(token.lemma_)
        doc_attr["pos"].append(token.pos_)
        doc_attr["tag"].append(token.tag_)
        doc_attr["dep"].append(token.dep_)
        doc_attr["shape"].append(token.shape_)
        doc_attr["alpha"].append(token.is_alpha)
        doc_attr["stop"].append(token.is_stop)

    # doc_df = pd.DataFrame(doc_attr)
    # print(doc_df)
    return displacy.render(doc, style="dep")


def match_sentences(sentences, filename: str):
    last_period_i = filename.rfind('.')
    output_file_name = filename[:last_period_i] + ".html"
    num_total = len(sentences)
    num_match = 0
    for i, sentence in enumerate(sentences):
        doc = nlp(sentence)
        matches = dependency_matcher(doc)

        if i == 0:
            file = open(output_file_name, "w")
            # file.write("These sentences should have matched. <br><br>\n")
        if matches:
            num_match += 1
            file.write(spaCy_parser(sentence))
            file.write(sentence + "<br>")
            file.write("Match!<br>")
        else:
            file.write(spaCy_parser(sentence))
            file.write(sentence + "<br>")
            file.write("No match<br>")

    file.write(f"{num_match}/{num_total} sentences matched.")
    file.close()
    print(f"Results saved in {output_file_name}")


def NBI(filename: str):
    with open(filename, "r") as csvfile:
        sentences = csvfile.readlines()
    for i, sentence in enumerate(sentences):
        sentences[i] = sentence[0:-1]
    match_sentences(sentences, filename)


if __name__ == "__main__":
    # sentences = [
    #     "I don't eat because I'm bored.",
    #     "She told her that they didn't go because of the storm.",
    #     "He did not go because of the rain.",
    #     "He hasn't eaten while I ate because the food was free.",
    #     "They chose not to stay in town because of the storm.",
    #     "This sentence should not be a match.",
    # ]

    NBI("n't_bec_randomized_for_first_150_DONE_negatives.txt")
    NBI("n't_bec_randomized_for_first_150_DONE_positives.txt")
    NBI("not_bec_randomized_for_first_150_DONE_negatives.txt")
    NBI("not_bec_randomized_for_first_150_DONE_positives.txt")

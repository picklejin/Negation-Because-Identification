not_because_dependency_patterns = [
    # not <neg VERB >mark because
    # neg_anchorVerb_markBec
    [
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
    ],

    # not <neg VERB >prep because
    # neg_anchorVerb_prepBec
    [
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
    ],

    # not <neg VERB >advcl VERB >mark because
    # neg_anchorVerb_advcl_markBec
    [
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
    ],

    # not <neg VERB >ccomp >advcl VERB >mark because
    # neg_anchorVerb_ccomp_advcl_markBec
    [
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
    ],

    # not <neg VERB >advcl >ccomp VERB >mark because
    # neg_anchorVerb_advcl_ccomp_markBec
    [
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
    ],

    # not <neg <ccomp VERB >advcl VERB >mark because
    # neg_ccomp_anchorVerb_advcl_markBec
    [
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
    ],

    # not <neg VERB >prep >prep because
    # neg_anchorVerb_prep_prepBec
    [
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
    ],

    # not <neg AUX >mark because
    # neg_anchorAux_markBec
    [
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
    ],

    # not <neg AUX >prep because
    # neg_anchorAux_prepBec
    [
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
    ],

    # not <neg AUX >advcl AUX >mark because
    # neg_anchorAux_advcl_markBec
    [
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
]

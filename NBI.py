from spacy.matcher import DependencyMatcher
from spacy import displacy
from not_because_dependency_patterns import *
import en_core_web_trf
import pandas as pd

nlp = en_core_web_trf.load(exclude=["lemmatizer"])
print("INFO: spaCy initialized successfully.")

"Initialize Dependency Matcher"
dependency_matcher = DependencyMatcher(nlp.vocab)
dependency_matcher.add("find match patterns", not_because_match_patterns)
dependency_forbidden = DependencyMatcher(nlp.vocab)
dependency_forbidden.add("find forbidden patterns", not_because_forbidden_patterns)
print("INFO: dependency_matcher initialized successfully.")


# Debug
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

    doc_df = pd.DataFrame(doc_attr)
    # print(doc_df)
    return str(displacy.render(doc, style="dep")) + "<br>\n" + doc_df.to_html() + "<br>\n"


def check_neg_because(doc: nlp) -> bool:
    """Ensure input sentence in nlp format has negation followed by "because" later in the sentence. """
    negation_i = -1
    because_i = -1
    doc_len = len(doc)
    # Get index of first negation
    for i, token in enumerate(doc):
        token_str = token.text.lower()
        if token_str == "not" or token_str == "n't":
            negation_i = i
            break
    # Get index of last because
    for i in range(doc_len - 1, -1, -1):
        token_str = doc[i].text.lower()
        if token_str == "because":
            because_i = i
            break
    if -1 < negation_i < because_i:
        return True
    else:
        return False


def match_sentences(sentences: list[str], filename: str):
    last_period_i = filename.rfind('.')
    output_file_name = filename[:last_period_i] + ".html"
    num_total = len(sentences)
    num_match = 0
    for i, sentence in enumerate(sentences):
        # # Debug
        # # test_patterns
        # # Test matcher
        # doc = nlp(sentence)
        # test_matcher = DependencyMatcher(nlp.vocab)
        # test_matcher.add("find test patterns", test_patterns)
        # match = dependency_matcher(doc) and not dependency_forbidden(doc) and test_matcher(doc)
        # if i == 0:
        #     file = open(output_file_name, "w")
        # if match:
        #     num_match += 1
        #     file.write(displacy.render(doc, style="dep"))
        #     file.write("\n" + sentence + "<br>\n")
        #     file.write("Match!<br>\n\n\n\n\n")
        # # else:
        # #     file.write(displacy.render(doc, style="dep"))
        # #     file.write("\n" + sentence + "<br>\n")
        # #     file.write("No match<br>\n\n\n\n\n")
        # continue

        # # Debug
        # # Dependency tree and detailed POS output
        # # POS details
        # if i == 0:
        #     file = open(output_file_name, "w")
        # file.write(spaCy_parser(sentence))
        # continue

        doc = nlp(sentence)
        # Determine whether sentence has a matching pattern in not_because_match_patterns
        # Return false if sentence has matching pattern in not_because_forbidden_patterns, or if sentence contains
        # "whether or not", or if sentence starts with "Not because",
        # or if there is not negation-because in the sentence.
        match = dependency_matcher(doc) and not dependency_forbidden(doc) and not (
                "whether or not" in sentence) and not sentence.startswith(
            "Not because") and check_neg_because(doc)

        if i == 0:
            file = open(output_file_name, "w")
        if match:
            num_match += 1
            if "negative" in filename:
                file.write(displacy.render(doc, style="dep"))
                file.write("\n" + sentence + "<br>\n")
                file.write("Match!<br>\n\n\n\n\n")
        else:
            if "positive" in filename:
                file.write(displacy.render(doc, style="dep"))
                file.write("\n" + sentence + "<br>\n")
                file.write("No match<br>\n\n\n\n\n")

    file.write(f"{num_match}/{num_total} sentences matched.")
    file.close()
    print(f"Results saved in {output_file_name}")


def NBI(filename: str):
    with open(filename, "r") as csvfile:
        sentences = csvfile.readlines()
    # Remove whitespace at end of sentence.
    for i, sentence in enumerate(sentences):
        sentences[i] = sentence[0:-1]
    match_sentences(sentences, filename)


if __name__ == "__main__":
    NBI("n't_bec_negatives.txt")
    NBI("n't_bec_positives.txt")
    NBI("not_bec_negatives.txt")
    NBI("not_bec_positives.txt")
    # NBI("test_negatives.txt")
    # NBI("test_positives.txt")

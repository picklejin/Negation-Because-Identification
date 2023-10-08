import numpy as np
import pandas as pd
import csv


def preformat(text: str) -> str:
    """Get rid of unnecessary punctuation marks and spaces.

    - " '" to "'"
    - " n'" to "n'"
    - "- " to ", "
    - " , " to ", "
    """
    from_str1 = " '"
    to_str1 = "'"
    from_str2 = " n'"
    to_str2 = "n'"
    # from_str3 = "- "
    # to_str3 = ", "
    from_str4 = " ,"
    to_str4 = ","
    from_str5 = ". \" "
    to_str5 = ".\" "
    from_str6 = " Mr . "
    to_str6 = " Mr. "
    from_str7 = " Mrs . "
    to_str7 = " Mrs. "
    from_str8 = " Ms . "
    to_str8 = " Ms. "
    from_str9 = " Dr . "
    to_str9 = " Dr. "
    from_str10 = " Prof . "
    to_str10 = " Prof. "
    from_str11 = " Gen . "
    to_str11 = " Gen. "
    from_str12 = " Rep . "
    to_str12 = " Rep. "
    from_str13 = " Sen . "
    to_str13 = " Sen. "
    from_str14 = " Gov . "
    to_str14 = " Gov. "
    from_str15 = " Hon . "
    to_str15 = " Hon. "
    from_str16 = " U .S. "
    to_str16 = " U.S. "

    #     assert type(text) == str, f"text data type is {type(text)}; {text}"
    post_format = (
        text.replace(from_str1, to_str1)
        .replace(from_str2, to_str2)
        # .replace(from_str3, to_str3)
        .replace(from_str4, to_str4)
        .replace(from_str5, to_str5)
        .replace(from_str6, to_str6)
        .replace(from_str7, to_str7)
        .replace(from_str8, to_str8)
        .replace(from_str9, to_str9)
        .replace(from_str10, to_str10)
        .replace(from_str11, to_str11)
        .replace(from_str12, to_str12)
        .replace(from_str13, to_str13)
        .replace(from_str14, to_str14)
        .replace(from_str15, to_str15)
        .replace(from_str16, to_str16)
        .lstrip()
    )
    return post_format

def postformat(text: str) -> str:
    """Remove space before final punctuation mark.
    Correct spacing around single and double quotes. 
    Remove space before colon.
    """
    text_list = text.split()
    last_index = len(text_list) - 1
    double_quote_begin = True
    single_quote_begin = True
    removal_indices = []

    for i, current_segment in enumerate(text_list):
        if i == last_index:
            text_list[i - 1] = text_list[i - 1] + current_segment
            text_list.pop()
        elif ('"' in current_segment):
            if(current_segment == '"'):
                if double_quote_begin:
                    text_list[i + 1] = current_segment + text_list[i + 1]
                    removal_indices.append(i)
                    double_quote_begin = False
                else:
                    text_list[i - 1] = text_list[i - 1] + current_segment
                    removal_indices.append(i)
                    double_quote_begin = True
            elif current_segment.endswith('"'):
                if double_quote_begin:
                    text_list[i] = text_list[i][0:-1]
                    text_list[i + 1] = '"' + text_list[i + 1]
                    double_quote_begin = False
                else: 
                    double_quote_begin = True
        elif (not current_segment.endswith("s'") and "'" in current_segment):
            if(current_segment == "'"):
                if single_quote_begin:
                    text_list[i + 1] = current_segment + text_list[i + 1]
                    removal_indices.append(i)
                    single_quote_begin = False
                else:
                    text_list[i - 1] = text_list[i - 1] + current_segment
                    removal_indices.append(i)
                    single_quote_begin = True
            elif current_segment.endswith("'"):
                if single_quote_begin:
                    text_list[i] = text_list[i][0:-1]
                    text_list[i + 1] = "'" + text_list[i + 1]
                    single_quote_begin = False
                else: 
                    single_quote_begin = True
        elif(current_segment == "("):
            text_list[i + 1] = current_segment + text_list[i + 1]
            removal_indices.append(i)
        elif(current_segment == ":"):
            text_list[i - 1] = text_list[i - 1] + current_segment
            removal_indices.append(i)
        elif(current_segment == ";"):
            text_list[i - 1] = text_list[i - 1] + current_segment
            removal_indices.append(i)
        elif(current_segment == ")"):
            text_list[i - 1] = text_list[i - 1] + current_segment
            removal_indices.append(i)
    
    for i in reversed(removal_indices):
        text_list.pop(i)
    
    return " ".join(text_list)
        

def end_with_space(text: str) -> str:
    if text == "":
        return text
    return text + " "

def add_double_quote(text: str) -> str:
    if text.count("\"") % 2:
        return text + " \""
    else:
        return text


# For use on "pre" column. Extract beginning parts of the sentence that continues into "match" column.
def extract_last_sentence(text: str) -> str:
    lst = text.split()

    for i in range(len(lst) - 1, -2, -1):
        if (
            lst[i] == "."
            or lst[i] == ".'"
            or lst[i] == ".\""
            or lst[i].find("@") > -1
            or lst[i].find(":") > -1
            or lst[i].find("?") > -1
            or lst[i].find("!") > -1
            or lst[i].find("#") > -1
            or lst[i].find("...") > -1
            or lst[i].find("--") > -1
        ):
            break

    list_index = i + 1
    new_list = []

    for i in range(list_index, len(lst)):
        new_list.append(lst[i])

    return " ".join(new_list)


# For use on "match" column. Extract the first sentence or portion not interuppted by special symbols.
def extract_first_sentence(text: str) -> str:
    lst = text.split()
    sentence_ended = False

    for i in range(len(lst)):
        if sentence_ended:
            break
        elif (
            lst[i] == "."
            # or lst[i] == "'"
            or lst[i] == ".'"
            or lst[i] == ".\""
            or lst[i].find("?") > -1
            or lst[i].find("!") > -1
            or lst[i].find("...") > -1
        ):
            sentence_ended = True
        # elif (
        #     lst[i].find("@") > -1
        #     or lst[i].find(":") > -1
        #     or lst[i].find("#") > -1
        #     or lst[i].find("--") > -1
        # ):
        #     break
        elif i == len(lst) - 1:
            i = len(lst)

    list_index = i
    new_list = []

    for i in range(list_index):
        new_list.append(lst[i])

    return " ".join(new_list)

def extract_first_punctuation(text: str) -> str:
    if type(text) != str:
        return ""
    elif text.startswith(", "):
        return ","
    elif text.startswith(". . . "):
        return "..."
    elif text.startswith("... "):
        return "..."
    elif text.startswith(". \" "):
        return ".\""
    elif text.startswith(". ' "):
        return ".'"
    elif text.startswith(". "):
        return "."
    elif text.startswith("? \" "):
        return "?\""
    elif text.startswith("? ' "):
        return "?'"
    elif text.startswith("? "):
        return "?"
    elif text.startswith("! \" "):
        return "!\""
    elif text.startswith("! ' "):
        return "!'"
    elif text.startswith("! "):
        return "!"
    else:
        return ""


def df_to_txt(df, test_file_name: str, separate=True, pos=True) -> None:
    if separate:
        if pos:
            file_name_extension = "_positives.txt"
        else:
            file_name_extension = "_negatives.txt"
    else:
        file_name_extension = ".txt"

    df.to_csv(
        path_or_buf=(test_file_name + file_name_extension),
        columns=["output"],
        header=False,
        index=False,
        quoting=csv.QUOTE_NONE,  # Prevents extra double quotes from being added
        sep="=",
    )


def coca_excel_to_txt(
    filepath, 
    test_file_name: str,
    must_contain: str,
    separate_pos_neg=True
) -> None:
    """Takes development set Excel file link. Writes two txt files separating hits and non-hits.

    Arguments
    - filepath: Any valid string path (including URL) or path like object
    - test_file_name: Desired txt file name, which will be followed by _positives.txt or _negatives.txt
    - include_pre: Whether you would like to extract beginning parts of the sentence in the "pre" column
      that continues into the "match" column.
    """
    # Get the full sentence of what's in the "match" column.
    df = pd.read_excel(io=filepath, usecols="B:E")
    df[df.columns[0]]=df[df.columns[0]].values.astype(str)
    df[df.columns[1]]=df[df.columns[1]].values.astype(str)
    df[df.columns[2]]=df[df.columns[2]].values.astype(str)
    df[df.columns[0]] = (
        df[df.columns[0]].apply(preformat).apply(extract_last_sentence).apply(end_with_space)
    )
    df[df.columns[1]] = (df[df.columns[1]].apply(end_with_space) + df[df.columns[2]]).apply(preformat).apply(extract_first_sentence)
    df["output"] = (df[df.columns[0]] + df[df.columns[1]]).apply(preformat)

    # Delete sentences that were interrupted midway
    df = df[df["output"].str.contains("@", regex=False) == False]
    df = df[df["output"].str.contains("#", regex=False) == False]
    # df = df[df["output"].str.contains("--", regex=False) == False]
    # df = df[df["output"].str.contains("-,", regex=False) == False]
    df = df[df["output"].str.contains("...", regex=False) == False]
    df = df[df["output"].str.contains("- ", regex=False) == False]
    df = df[df["output"].str[0].str.isupper()]
    df = df[
        df["output"].str.contains("( censored )", regex=False) == False
    ]  # Ambiguous what word it's taking place for; could be noun, verb, adj, etc.
    df = df[
        df["output"].str.contains("( UNINTELLIGIBLE  )", regex=False) == False
    ]
    df = df[df["output"].str.contains(must_contain) == True]
    df["output"] = df["output"].apply(postformat)

    # Export to txt
    if separate_pos_neg:
        # https://stackoverflow.com/a/46572999
        other_df, negative_df = [x for _, x in df.groupby(df[df.columns[-2]] == "no")]
        other_df, positive_df = [x for _, x in df.groupby(df[df.columns[-2]] == "yes")]

        df_to_txt(positive_df, test_file_name=test_file_name, separate=True, pos=True)
        df_to_txt(negative_df, test_file_name=test_file_name, separate=True, pos=False)
    else:
        df_to_txt(df, test_file_name=test_file_name, separate=False)


if __name__ == "__main__":
    coca_excel_to_txt(
        filepath="anyn't_incomplete_Aadya.xlsx",
        test_file_name="any_n't",
        must_contain="n't",
        separate_pos_neg=True,
    )
    coca_excel_to_txt(
        filepath="anynot_incomplete_Meadow.xlsx",
        test_file_name="any_not",
        must_contain="not",
        separate_pos_neg=True,
    )

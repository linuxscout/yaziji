#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  
#  Copyright 2020 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os.path
import sys

import argparse
import pandas as pd

sys.path.append(os.path.join("../yaziji"))
#~ sys.path.append(os.path.join("../"))

import phrase_generator
import components_set
import json
DEFAULT_FILE = os.path.join(os.path.dirname(__file__), "samples/samples40.json")

from utils import open_file
def grabargs():
    parser = argparse.ArgumentParser(description='Test Yaziji phrase generateor.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=False,
    help="input file to convert", metavar="FILE")
    
    parser.add_argument("-o", dest="outfile", nargs='?', 
        help="Output file to convert", metavar="OUTFILE")
    parser.add_argument("-c", dest="command", nargs='?', default="test",
        help="Command to run (test, generate, eval)", metavar="COMMAND")
    parser.add_argument("--limit", type=int, nargs='?',default = 1000,
                        help="Limit line to treat", metavar="LIMIT")
    args = parser.parse_args()
    return args
    
def build_phrase(options):
    """
    return a dict
    :param options:
    :return:
    """
    options = dict(options)
    phraser = phrase_generator.PhraseGenerator()
    components = options
    result = phraser.build(components)
    phrase = result.get("phrase")
    # print(u"".join(["<%s>"%x for x in components.values()]))
    # print(phraser.pattern.stream.__str__())
    # return phrase
    return result

def get_data():
    """
    """
    dataset =[
        {
        'place': 'سوق', 'negative': 'منفي', 'voice': 'مبني للمجهول', 'subject': 'أنت', 'auxiliary': '', 'tense': 'المضارع المعلوم', 'verb': 'ضَرِبَ', 'action': 'sample', 'object': 'بَابٌ', 'text': 'أنت', 'time': 'كل يوم'
        },
        
        
        {'verb': 'شَرِبَ', 'time': 'دائما', 'subject': 'هو', 'text': 'هو', 'auxiliary':u'اِسْتَطَاعَ', 'tense': 'المضارع المعلوم', 'voice': 'معلوم', 'object': 'حَلِيبٌ', 'action': 'sample', 'place': 'بيت', 'negative': 'مثبت'},
            {'time': 'بَعْدَ غَدٍ', 'place': '', 'text': 'أنتن', 'action': 'sample', 'tense': 'الماضي المعلوم', 'auxiliary': 'اِسْتَطَاعَ', 'voice': 'معلوم', 'negative': 'مثبت', 'verb': 'ضَرِبَ', 'subject': 'أنتن', 'object': 'حَلِيبٌ'
        },
        {'time': 'دَائِمًا', 'place': '', 'text': 'هو', 'action': 'sample', 'tense': 'الماضي المعلوم', 'auxiliary': 'اِسْتَطَاعَ', 'voice': 'معلوم', 'negative': 'منفي', 'verb': 'شَرِبَ', 'subject': 'هو', 'object': 'حَلِيبٌ'}
        ,
        {'verb': 'قَالَ', 'phrase_type': 'جملة اسمية', 'auxiliary': 'أَرَادَ', 'place': 'سوق', 'object': '', 'voice': 'معلوم', 'text': 'هو', 'action': 'sample', 'time': 'غَدًا', 'subject': 'هو', 'negative': 'مثبت', 'tense': 'الماضي المعلوم'}
        ,
        {'text': 'أَحْمَد', 'auxiliary': 'أَرَادَ', 'time': 'غَدًا', 'place': 'سوق', 'negative': 'مثبت', 'action': 'sample', 'tense': 'الماضي المعلوم', 'subject': 'أَحْمَد', 'object': 'حَلِيبٌ', 'verb': 'قَالَ', 'voice': 'معلوم', 'phrase_type': 'جملة اسمية'}
        ,
        ]    
    return dataset
def show(data):
    print("inside date")
    print(dict(data))
    return "inside data"


def read_data(infile):
    # tests data from file or from data set
    if not infile:
        infile = DEFAULT_FILE
    dataset = open_file(infile)
    if dataset is None:
        dataset = get_data()
        dataset = pd.DataFrame(dataset)
    return dataset

def treat_data(df, command, infile):
    """
    treat data
    :param df:
    :param command:
    :param infile:
    :return:
    """
    # df["output"] = df.apply(build_phrase, axis=1)
    # if command == "test" and infile:
    #     df["eval"] = df.apply(lambda x: x['target'] == x["output"], axis=1)
    # return df
    # Columns to exclude
    exclude_columns = ['phrase', 'inflection', 'errors', "valid"]

    # Select columns except the excluded ones
    columns_to_apply = df.columns.difference(exclude_columns)

    # Apply an operation (e.g., multiply by 2) on the selected columns
    # df["output"] = df[columns_to_apply].apply(build_phrase, axis=1)
    result = df[columns_to_apply].apply(build_phrase, axis=1)
    # Convert the resulting Series of dicts into a DataFrame and concatenate
    expanded_columns = pd.DataFrame(result.tolist())
    # Add a prefix to column names
    expanded_columns = expanded_columns.add_prefix("out_")
    df = pd.concat([df, expanded_columns], axis=1)

    if command == "test":
        df["eval"] = df.apply(lambda x: x['phrase'] == x["out_phrase"], axis=1)
    return df


def main(args):
    args = grabargs()
    command = args.command
    limit = args.limit
    infile = args.filename
    outfile = args.outfile
    print(command, limit, infile, outfile)
    #~ sys.exit()
    if command == "generate":
        # generate a data set
        compo = components_set.componentsSet()
        dataset = compo.get_random(10)
        df = pd.DataFrame(dataset)        
    else:
        # read data from file or return a defined data
        df = read_data(infile)
    # avoid NaN values
    df = treat_data(df, command, infile)
    # df["output"] = df.apply(build_phrase, axis = 1)
    # if command ==  "test" and infile:
    #     df["eval"] = df.apply(lambda x: x['target']==x["output"],axis=1)
     
    # pandas
    if outfile:
        df.to_csv(outfile, encoding="utf8", sep="\t")
    else:
        print(df)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python3

"""
Do a local practice grading.
The score you recieve here is not an actual score,
but gives you an idea on how prepared you are to submit to the autograder.
"""

import json
import os
import sys

import pandas

import autograder.question
import autograder.assignment
import autograder.style

THIS_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH = os.path.join(THIS_DIR, 'cia_world_factbook_2022.json')

class HO3(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        with open(DATA_PATH, 'r') as file:
            data = json.load(file)

        world_data = pandas.DataFrame.from_dict(data, orient = 'index')
        world_data.sort_index(axis = 0, inplace = True)
        world_data.insert(0, 'Country', world_data.index)
        world_data.reset_index(drop = True, inplace = True)

        super().__init__(
            name = 'Practice Grading for Hands-On 3',
            additional_data = {
                'world_data': world_data,
            }, questions = [
                T1A(1, "Task 1.A (drop_sparse_columns)"),
                T1B(1, "Task 1.B (extract_numbers)"),
                T1C(1, "Task 1.C (guess_types)"),
                T2A(1, "Task 2.A (find_outliers)"),
                T2B(1, "Task 2.B (merge_columns)"),
                T3A(1, "Task 3.A (one_hot)"),
                T4A(1, "Task 4.A (left_join)"),
                autograder.style.Style(kwargs.get('input_dir'), max_points = 1),
            ], **kwargs)

class T1A(autograder.question.Question):
    def score_question(self, submission, world_data):
        result = submission.__all__.drop_sparse_columns(world_data, 0.50)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        self.full_credit()

class T1B(autograder.question.Question):
    def score_question(self, submission, world_data):
        result = submission.__all__.extract_numbers(world_data, ['Country', 'Export commodities'])
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        self.full_credit()

class T1C(autograder.question.Question):
    def score_question(self, submission, world_data):
        result = submission.__all__.guess_types(world_data)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        self.full_credit()

class T2A(autograder.question.Question):
    def score_question(self, submission, world_data):
        frame = pandas.DataFrame({'Label': ['1', '2', '3', '4'], 'A': [1.0, 1.5, 2.0, 100.0]})

        result = submission.__all__.find_outliers(frame, 1.0, 'Label')
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, dict)):
            self.fail("Answer must be a dict.")
            return

        if (len(result) == 0):
            self.fail("Could not find any outliers.")
            return

        key = list(result.keys())[0]
        if (len(result[key]) == 0):
            self.fail("Got an outlier list that is empty.")
            return

        if (not isinstance(result[key][0], tuple)):
            self.fail("List values should be tuples.")
            return

        if (len(result[key][0]) != 2):
            self.fail("List values should be tuples of length 2.")
            return

        self.full_credit()

class T2B(autograder.question.Question):
    def score_question(self, submission, world_data):
        test_data = {
            'Values_1': [1],
            'Values_2': [2]
        }
        test_frame = pandas.DataFrame(test_data)
        result = submission.__all__.merge_columns(test_frame.copy(), ['Values_1', 'Values_2'],
                'Mean')

        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        self.full_credit()

class T3A(autograder.question.Question):
    def score_question(self, submission, world_data):
        result = submission.__all__.one_hot(world_data, 'Export commodities')
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        if ((list(result.columns) == list(world_data.columns)) and (result == world_data)):
            self.fail("Answer should be a NEW DataFrame.")
            return

        self.full_credit()

class T4A(autograder.question.Question):
    def score_question(self, submission, world_data):
        lhs = pandas.DataFrame({'ID': [0, 1, 2], 'A': [1, 2, 3]})
        rhs = pandas.DataFrame({'B': [4, 5, 6]})

        result = submission.__all__.left_join(lhs, rhs, ['ID'])
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        if (((list(result.columns) == list(lhs.columns)) and (result == lhs))
                or ((list(result.columns) == list(rhs.columns)) and (result == rhs))):
            self.fail("Answer should be a NEW DataFrame.")
            return

        self.full_credit()

def main(path):
    assignment = HO3(input_dir = path)
    result = assignment.grade()

    print("***")
    print("This is NOT an actual grade, submit to the autograder for an actual grade.")
    print("***\n")

    print(result.report())

def _load_args(args):
    exe = args.pop(0)
    if (len(args) != 1 or ({'h', 'help'} & {arg.lower().strip().replace('-', '') for arg in args})):
        print("USAGE: python3 %s <submission path (.py or .ipynb)>" % (exe), file = sys.stderr)
        sys.exit(1)

    path = os.path.abspath(args.pop(0))

    return path

if (__name__ == '__main__'):
    main(_load_args(list(sys.argv)))

#!/usr/bin/env python3

"""
Do a local practice grading.
The score you recieve here is not an actual score,
but gives you an idea on how prepared you are to submit to the autograder.
"""

import os
import sys

import numpy
import pandas

import autograder.assignment
import autograder.question
import autograder.style

THIS_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH = os.path.join(THIS_DIR, 'synthetic_covid_data.csv')

class HO1(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        super().__init__(
            name = 'Practice Grading for Hands-On 1',
            additional_data = {
                'synthetic_data': pandas.read_csv(DATA_PATH, index_col = 'id')
            }, questions = [
                T0A(1, "Task 0.A (select_column)"),
                T0B(1, "Task 0.B (filter_rows)"),
                T0C(1, "Task 0.C (add_column)"),
                T0D(1, "Task 0.D (drop_column)"),
                T0E(1, "Task 0.E (concat_frames)"),
                T1A(1, "Task 1.A (collection_to_inverted_dict)"),
                T1B(1, "Task 1.B (ndarray_to_dict)"),
                T1C(1, "Task 1.C (frame_to_dict)"),
                T2A(1, "Task 2.A (count_infected)"),
                T2B(1, "Task 2.B (count_symptomatic)"),
                T2C(1, "Task 2.C (mean_days)"),
                T3A(1, "Task 3.A (fraction_infected)"),
                T3B(1, "Task 3.B (fraction_symptomatic)"),
                T3C(1, "Task 3.C (count_special_uninfected)"),
                T3D(1, "Task 3.D (fraction_isoantigenic)"),
                T4A(1, "Task 4.A (add_isoantigenic_column)"),
                T5A(1, "Task 5.A (prep_scatter)"),
                T6A(1, "Task 6.A (rmse)"),
                autograder.style.Style(kwargs.get('input_dir'), max_points = 1),
            ], **kwargs)

class T0A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.select_column(synthetic_data, 'titer')
        self.check_not_implemented(result)

        if (not isinstance(result, pandas.Series)):
            self.fail("Answer must be a column.")

        self.full_credit()

class T0B(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.filter_rows(synthetic_data, 'titer', 32)
        self.check_not_implemented(result)

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")

        self.full_credit()

class T0C(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.add_column(pandas.DataFrame(), 'test', [])
        self.check_not_implemented(result)

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")

        self.full_credit()

class T0D(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.drop_column(synthetic_data.copy(), 'titer')
        self.check_not_implemented(result)

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")

        self.full_credit()

class T0E(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.concat_frames(pandas.DataFrame(), pandas.DataFrame())
        self.check_not_implemented(result)

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")

        self.full_credit()

class T1A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        collection_to_inverted_dict = submission.__all__.collection_to_inverted_dict

        result = collection_to_inverted_dict(['1', '2'])
        self.check_not_implemented(result)

        if (not isinstance(result, dict)):
            self.fail("Result must be a dict.")

        # [(input, expected, feedback), ...]
        test_cases = [
            (['a', 'b', 'c'], {'a': 0, 'b': 1, 'c': 2}, 'basic list'),
        ]

        self.full_credit()

        for (value, expected, feedback) in test_cases:
            actual = collection_to_inverted_dict(value)
            if (expected != actual):
                self.add_message("Missed test case '%s'." % (feedback), add_score = -1)

        self.cap_score()

class T1B(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        ndarray_to_dict = submission.__all__.ndarray_to_dict

        result = ndarray_to_dict(numpy.array(['1', '2']))
        self.check_not_implemented(result)

        if (not isinstance(result, dict)):
            self.fail("Result must be a dict.")

        # [(input, expected, feedback), ...]
        test_cases = [
            (
                [['a', 'b'], ['c', 'd']],
                {(0, 0): 'a', (0, 1): 'b', (1, 0): 'c', (1, 1): 'd'},
                'basic array',
            ),
        ]

        self.full_credit()

        for (value, expected, feedback) in test_cases:
            actual = ndarray_to_dict(numpy.array(value))
            if (expected != actual):
                self.add_message("Missed test case '%s'." % (feedback), add_score = -2)

        self.cap_score()

class T1C(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        frame_to_dict = submission.__all__.frame_to_dict

        result = frame_to_dict(pandas.DataFrame(['1', '2']))
        self.check_not_implemented(result)

        if (not isinstance(result, dict)):
            self.fail("Result must be a dict.")

        # [(input, expected, feedback), ...]
        test_cases = [
            (
                {'A': ['1', '2'], 'B': ['3', '4']},
                {('A', 0): '1', ('A', 1): '2', ('B', 0): '3', ('B', 1): '4'},
                'basic frame',
            ),
        ]

        self.full_credit()

        for (value, expected, feedback) in test_cases:
            actual = frame_to_dict(pandas.DataFrame(value))
            if (expected != actual):
                self.add_message("Missed test case '%s'." % (feedback), add_score = -2)

        self.cap_score()

class T2A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.count_infected(synthetic_data)
        self.check_not_implemented(result)

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")

        self.full_credit()

class T2B(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.count_symptomatic(synthetic_data)
        self.check_not_implemented(result)

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")

        self.full_credit()

class T2C(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.mean_days(synthetic_data)
        self.check_not_implemented(result)

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")

        self.full_credit()

class T3A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.fraction_infected(synthetic_data)
        self.check_not_implemented(result)

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")

        self.full_credit()

class T3B(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.fraction_symptomatic(synthetic_data)
        self.check_not_implemented(result)

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")

        self.full_credit()

class T3C(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.count_special_uninfected(synthetic_data)
        self.check_not_implemented(result)

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")

        self.full_credit()

class T3D(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.fraction_isoantigenic(synthetic_data)
        self.check_not_implemented(result)

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")

        self.full_credit()

class T4A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.add_isoantigenic_column(synthetic_data)
        self.check_not_implemented(result)

        if ('isoantigenic' not in result):
            self.fail("Isoantigenic column is missing.")

        self.full_credit()

class T5A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.prep_scatter(synthetic_data, 'days_before_symptoms',
                'titer', 'X', 'Y')

        self.check_not_implemented(result)

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")

        self.full_credit()

class T6A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        predictions = [1, 1, 0, 0]
        labels = [1, 0, 1, 0]

        result = submission.__all__.rmse(predictions, labels)
        self.check_not_implemented(result)

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")

        self.full_credit()

def main(path):
    assignment = HO1(input_dir = path)
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

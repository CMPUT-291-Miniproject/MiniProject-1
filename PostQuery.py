from collections import namedtuple
"""
Definitions for namedtuple objects to make handling
posts easier
"""
QuestionQuery = namedtuple('QuestionQuery', ['title', 'voteCount', 'answerCount', 'body', 'pid'])
AnswerQuery = namedtuple('AnswerQuery', ['title', 'voteCount', 'body', 'pid'])
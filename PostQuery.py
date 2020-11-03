from collections import namedtuple

QuestionQuery = namedtuple('QuestionQuery', ['title', 'voteCount', 'answerCount', 'body', 'pid'])
AnswerQuery = namedtuple('AnswerQuery', ['title', 'voteCount', 'body', 'pid'])
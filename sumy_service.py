from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

# from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
stemmer = Stemmer(LANGUAGE)

class SumyService:

  def __init__(self):
    self.summarizer = Summarizer(stemmer)
    self.summarizer.stop_words = get_stop_words(LANGUAGE)

  def call(self, text, sentences_count):
    result = []
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    summarizer_result = self.summarizer(parser.document, sentences_count)
    print('got summarizer result: ', summarizer_result)
    for sentence in summarizer_result:
      result.append(str(sentence))

    return { 'result': result }
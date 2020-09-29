from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

# from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer as LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sb_email_text_parser import SbEmailTextParser

LANGUAGE = "english"
stemmer = Stemmer(LANGUAGE)

class SumyService:

  def __init__(self):
    self.lsa_summarizer = LsaSummarizer(stemmer)
    self.lex_rank_summarizer = LexRankSummarizer(stemmer)
    self.lsa_summarizer.stop_words = get_stop_words(LANGUAGE)
    self.lex_rank_summarizer.stop_words = get_stop_words(LANGUAGE)
    self.email_text_parser = SbEmailTextParser()

  def __call__(self, text, sentences_count, method="lsa"):
    result = []
    parsed_text = self.email_text_parser(text)
    parser = PlaintextParser.from_string(parsed_text, Tokenizer(LANGUAGE))
    if method == "lex":
      summarizer_result = self.lex_rank_summarizer(parser.document, sentences_count)
    else:
      summarizer_result = self.lsa_summarizer(parser.document, sentences_count)
    for sentence in summarizer_result:
      result.append(str(sentence))

    return { 'result': result }
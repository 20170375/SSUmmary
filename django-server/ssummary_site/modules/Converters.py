from .Translaters import *
from .Summarizers import *

import time

from hanspell import spell_checker


class MyConverter:
    def __init__(self):
        # initialize translater instance
        # self.translater = Translater_with_papago_api()
        self.translater = Translater_with_googletrans()
        print("=" * 50)
        print("Log: translater 초기화 성공")       

        # initialize summarizer instance
        # self.summarizer = Summarizer_with_KoBart()
        # self.summarizer = Summarizer_with_Bart_r3f()
        self.summarizer = Summarizer_with_textrank()
        print("Log: summarizor 초기화 성공")
        print("=" * 50, end="\n\n")

    def translate(self, text, target, input_size=5000, debug=0):
        """
        Translate the text into Korean by dividing it into chunks.

        Args:
            text (str): Text to be translated
            target (str): Target language
            input_size (int): Size of each chunk
            debug (int): Debug level
        """
        start = time.time()
        result = self.translater.translate(text, target, input_size=input_size)
        if debug == 1:
            print("번역 소요시간:", time.time() - start)
        return result

    def spell_check(self, text, input_size=500, debug=0):
        """
        Check the spelling of the text.

        Args:
            text (str): Text to be checked
            input_size (int): Size of each chunk
            debug (int): Debug level
        """
        start = time.time()

        result = ""
        dumps = divide(text, input_size=input_size)

        for dump in dumps:
            try:
                result += spell_checker.check(dump).checked
            except Exception as e:
                print("ERROR from spell_check(): \n" + dump)
                raise e

        if debug == 1: 
            print("검사 소요시간:", time.time() - start)
        return result

    def summarize(self, text, input_size=1024, deep=False, debug=0):
        """
        Summarize the text by dividing it into chunks.

        args:
            text (str): Text to be translated
            input_size (int): Size of each chunk
            deep (bool): Whether to use deep summarization
            debug (int): Debug level
        """
        start = time.time()
        result = self.summarizer.generate(text, input_size=input_size, deep=deep)
        if debug == 1: 
            print("깊은" if deep == True else "얕은", "요약 소요시간:", time.time() - start)
        return result

from django.shortcuts import render
from django.http import JsonResponse

from .modules.Converters import MyConverter

# initialize converter instance
converter = MyConverter()

#--- Function-based View
def ssummary(request):
    if request.method == 'POST':
        text = request.POST['content']
        deep = True if request.POST['deep'] == 'true' else False
        target_lang = request.POST['target_lang']

        debug = 1
        if debug == 1:
            print()
        text_kor = converter.translate(text, 'ko', input_size=5000, debug=debug) # 번역
        text_checked_kor = converter.spell_check(text_kor, debug=debug) # 문법 검사
        text_sum = converter.summarize(text_checked_kor, deep=deep, debug=debug) # 요약
        text_res = converter.translate(text_sum, target_lang, input_size=5000, debug=debug) # 번역

        # JSON 객체 생성
        result = {
            'text': text_res,
            'deep': deep,
            'target_lang': target_lang
        }

        # send response as JSON
        return JsonResponse(result)

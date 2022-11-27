# URL: https://leetcode.com/problems/html-entity-parser/
# Задание: на ввод подаётся код HTML, на выходе нужно получить читабельную строку с заменой символов
# на их обычное представление.
# Суть проблемы: два идентичных решения, одно в котором идёт распаковка списка кортежей,
# во втором- пар "ключ" - "значение" из словаря. Метод через список работает, через словарь не работает.
# При построчном выводе элементов кортежей и ключей словаря
# и дальнейшем сравнении получаем True- элементы идентичны.


import re


class Solution(object):
    def entityparser(self, text):
        """
        :type text: str
        :rtype: str
        """
        di = {'&quot;': '\"', '&apos;': '\'', '&amp;': '&', '&gt;': '>', '&lt;': '<', '&frasl;': '/'}

        for key, value in di.items():
            text = re.sub(key, value, text)

        return text

    def entitytuple(self, text):
        entities = [('&quot;', '\"'), ('&apos;', '\''), ('&gt;', '>'), ('&lt;', '<'), ('&frasl;', '/'), ('&amp;', '&')]

        for pat, repl in entities:
            text = re.sub(pat, repl, text)

        return text


class TestCases(object):
    def test_two_funcs(self, txt: str):
        with_list = Solution().entitytuple(text=txt)
        with_dict = Solution().entityparser(text=txt)
        assert with_dict == with_list


if __name__ == '__main__':
    stri = "&amp; is an HTML entity but &ambassador; is not."
    method_with_dict = Solution().entityparser(text=stri)
    method_with_list = Solution().entitytuple(text=stri)
    print(method_with_dict)
    print(method_with_list)

    our_test = TestCases().test_two_funcs(stri)

    print('thanx for help')

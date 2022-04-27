from cgi import test
import enum
import json
from unittest import result
from typing import List
from separate import separate_japanese
from special_chars import special_chars


class Translator:
    def __init__(self, self_phi_filepath='self_phi.txt', pair_phi_filepath='pair_phi.txt', dictionary_filepath='dictionary.txt') -> None:
        self.self_phi = self.get_dict(self_phi_filepath)
        self.pair_phi = self.get_dict(pair_phi_filepath)
        self.word_dict = self.get_dict(dictionary_filepath)

    def get_dict(self, filepath): # 从文件读取字典
        file = open(filepath, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        
        return json.loads(content)

    def get_all_romaji_choices(self, words: list, word_dict: dict):
        choices = ['']
        for word in words:
            new_choices = []
            romajis = word_dict[word]
            for romaji in romajis:
                for choice in choices:
                    new_choices.append(choice + '|' + romaji)
            choices = new_choices
        for i, choice in enumerate(choices):
            choices[i] = choices[i][1:]
        return choices


    def calc_score(self, words:list, romajis:list):
        self.self_phi['っ'] = {'っ': 1}
        # 计算自势函数值
        self_val = 1
        for i, word in enumerate(words):
            self_val *= self.self_phi[word][romajis[i]]
        # 计算相邻势函数值
        pair_val = 1
        start_word = '<start>'
        end_word = '<end>'
        for i in range(len(words)):
            # get word_pair and romaji_pairs
            word_pair = ''
            romaji_pair = ''
            if i == 0:
                word_pair = start_word + '|' + words[i]
                romaji_pair = start_word + '|' + romajis[i]
            elif i == len(words) - 1:
                word_pair = words[i] + '|' + end_word
                romaji_pair = romajis[i] + '|' + end_word
            else:
                word_pair = words[i - 1] + '|' + words[i]
                romaji_pair = romajis[i - 1] + '|' + romajis[i]
            if word_pair in self.pair_phi.keys() and romaji_pair in self.pair_phi[word_pair].keys():
                pair_val *= self.pair_phi[word_pair][romaji_pair]
        return self_val * pair_val


    def get_romaji_from_pure_words(self, words: list) -> str:
        all_romaji_choices = self.get_all_romaji_choices(words, self.word_dict) # 找到所有可能的罗马音组合
        # 给所有组合按照MRF打分，找到最好的一种组合
        max_score = 0
        best_choice = ''
        for i in range(len(all_romaji_choices)):
            score = self.calc_score(words, all_romaji_choices[i].split('|'))
            if score > max_score:
                max_score = score
                best_choice = all_romaji_choices[i]
        # 拆掉分隔符，把っ替换为后面的字母
        romajis = best_choice.split('|')
        result = ''
        for i, c in enumerate(romajis):
            if c == 'っ':
                result += romajis[i + 1][0]
            else:
                result += c + ' '
        return result
    

    def get_romaji_from_pure_japanese(self, japanese: str) -> str:
        words = separate_japanese(japanese, self.word_dict)
        return self.get_romaji_from_pure_words(words)
    
    def is_legal_char(self, c) -> bool:
        if c in special_chars:
            return False
        if c in self.word_dict.keys():
            return True
        return False

    def get_romaji_from_japanese(self, japanese: str) -> str:
        # 首先分成合法和不合法的部分
        japanese_pieces = []
        legal_record = []
        is_last_legal = None
        for c in japanese:
            is_cur_legal = self.is_legal_char(c)
            if is_last_legal is None:
                japanese_pieces.append(c)
                legal_record.append(is_cur_legal)
            elif is_cur_legal == is_last_legal:
                japanese_pieces[-1] += c
            else:
                japanese_pieces.append(c)
                legal_record.append(is_cur_legal)
            is_last_legal = is_cur_legal
        # 合法的部分进行转换，不合法的直接复制下来
        result = ''
        for i, japanese_piece in enumerate(japanese_pieces):
            if legal_record[i]:
                result += self.get_romaji_from_pure_japanese(japanese_piece)
            else:
                result += japanese_piece
        # 去掉连续的空格
        while '  ' in result:
            result = result.replace('  ', ' ')
        return result


if __name__ == '__main__':
    translator = Translator()
    test_japanese = '今宵は灯火がいくつ辿り着くのだろう'
    romaji = translator.get_romaji_from_japanese(test_japanese)
    print(romaji)
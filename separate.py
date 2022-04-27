import MeCab


mecab = MeCab.Tagger ("-Owakati")


def separate_japanese_longest_front(japanese: str, word_dict: dict):
    result = []
    # 最长前缀匹配
    start = 0
    end = len(japanese)
    while start < end:
        longest_end = start + 1
        
        for i in range(1, end - start + 1):
            if japanese[start: start + i] in word_dict.keys():
                longest_end = start + i
        result.append(japanese[start: longest_end])
        start = longest_end
    return result


def separate_japanese_mecab(japanese: str) -> str:
    return mecab.parse(japanese).split(' ')[:-1]


def separate_japanese(japanese: str, word_dict: dict):
    # 先用mecab分词
    result = separate_japanese_mecab(japanese)
    # 检查每个词，如果词典里没有，再用最长前缀匹配分词
    new_result = []
    keys = word_dict.keys()
    for word in result:
        if not word in keys:
            new_words = separate_japanese_longest_front(word, word_dict)
            for new_word in new_words:
                new_result.append(new_word)
        else:
            new_result.append(word)

    return new_result
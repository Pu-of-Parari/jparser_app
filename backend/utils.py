import MeCab

def wakati(text):
    '''分かち書き用関数
    input  << text : 入力テキスト
    output >> m.parse(wakatext) : 分かち済みテキスト'''
    wakatext = text
    m = MeCab.Tagger('-Owakati')
    #m = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/ipadic')#normal ipadic辞書指定
    return m.parse(wakatext).replace("\n","")

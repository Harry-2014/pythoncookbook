'''
2.18 字符串令牌解析
问题
你有一个字符串，想从左至右将其解析为一个令牌流。
解决方案
假如你有下面这样一个文本字符串：
'''
text = 'foo = 23 + 42 * 10'
'''
为了令牌化字符串，你不仅需要匹配模式，还得指定模式的类型。比如，你可能想
将字符串像下面这样转换为序列对：
'''
tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
'''
为了执行这样的切分，第一步就是像下面这样利用命名捕获组的正则表达式来定
义所有可能的令牌，包括空格
'''
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
'''
下一步，为了令牌化，使用模式对象很少被人知道的scanner() 方法。这个方法
会创建一个scanner 对象，在这个对象上不断的调用match() 方法会一步步的扫描目
标文本，每步一个匹配。
'''
scanner = master_pat.scanner('foo = 42')
print(scanner.match())

from collections import  namedtuple
def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

'''
如果你想过滤令牌流，你可以定义更多的生成器函数或者使用一个生成器表达式
'''
tokens = (tok for tok in generate_tokens(master_pat, text)
if tok.type != 'WS')
for tok in tokens:
    print(tok)
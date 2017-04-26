#encoding:utf-8
#导入字符串配对的包
import re
amount={}
resultPath='/home/chx/文档/树蛙/zy1/results.txt'
def comment(txt):
    with open(txt,'r')as file:
        comments=file.read()
        return comments


comments=comment('/home/chx/文档/树蛙/zy1/太空旅客.txt')

def dict(txt):
    with open(txt,'r')as readFile:
        for line in readFile.readlines():
            line = line.strip('\n')
            results = re.findall(line, comments)
            num = len(results)
            amount[line]=num
    with open(txt,'a')as writeFile:
        for line in amount:
            writeFile.write(str(amount[line]))
            writeFile.write(' ')
            writeFile.write(line)
            writeFile.write('\n')





dict('/home/chx/文档/树蛙/zy1/词典/角色/反派.txt')
dict('/home/chx/文档/树蛙/zy1/词典/角色/角色.txt')
dict('/home/chx/文档/树蛙/zy1/词典/角色/角色中的其他.txt')
dict('/home/chx/文档/树蛙/zy1/词典/角色/男主角.txt')
dict('/home/chx/文档/树蛙/zy1/词典/角色/配角.txt')
dict('/home/chx/文档/树蛙/zy1/词典/剧情/发展.txt')
dict('/home/chx/文档/树蛙/zy1/词典/剧情/结局.txt')
dict('/home/chx/文档/树蛙/zy1/词典/剧情/剧情.txt')
dict('/home/chx/文档/树蛙/zy1/词典/剧情/开头.txt')
dict('/home/chx/文档/树蛙/zy1/词典/剧情/泪点.txt')
dict('/home/chx/文档/树蛙/zy1/词典/剧情/笑点.txt')
dict('/home/chx/文档/树蛙/zy1/词典/视听/动作.txt')
dict('/home/chx/文档/树蛙/zy1/词典/视听/画面.txt')
dict('/home/chx/文档/树蛙/zy1/词典/视听/镜头.txt')
dict('/home/chx/文档/树蛙/zy1/词典/视听/视听.txt')
dict('/home/chx/文档/树蛙/zy1/词典/视听/试听效果中的其他.txt')
dict('/home/chx/文档/树蛙/zy1/词典/视听/音乐.txt')
dict('/home/chx/文档/树蛙/zy1/词典/制作/编剧.txt')
dict('/home/chx/文档/树蛙/zy1/词典/制作/出品公司.txt')
dict('/home/chx/文档/树蛙/zy1/词典/制作/导演.txt')
dict('/home/chx/文档/树蛙/zy1/词典/制作/选景.txt')
dict('/home/chx/文档/树蛙/zy1/词典/制作/制作.txt')
dict('/home/chx/文档/树蛙/zy1/词典/主题/风格.txt')
dict('/home/chx/文档/树蛙/zy1/词典/主题/题材内容.txt')
dict('/home/chx/文档/树蛙/zy1/词典/主题/主题.txt')



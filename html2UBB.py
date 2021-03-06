#coding:utf8
#将获取到的内容转换成UBB编码，即转换成可以直接发到discuz论坛可识别的内容代码
import re
def Html2UBB(content):
    #以下是将html标签转为ubb标签
    pattern = re.compile( '<a href=\"([sS]+?)\"[^>]*>([sS]+?)</a>',re.I)
    content = pattern.sub(r'[url=1]2[/url]',content)
    pattern = re.compile( '<img[^>]+src=\"([^\"]+)\"[^>]*>',re.I)
    content = pattern.sub(r'[img]1[/img]',content)
    pattern = re.compile( '<strong>([sS]+?)</strong>',re.I)
    content = pattern.sub(r'[b]1[/b]',content)
    pattern = re.compile( '<font color=\"([sS]+?)\">([sS]+?)</font>',re.I)
    content = pattern.sub(r'[1]2[/1]',content)
    pattern = re.compile( '<[^>]*?>',re.I)
    content = pattern.sub('',content)
    #以下是将html转义字符转为普通字符
    content = content.replace('<','<')
    content = content.replace('>','>')
    content = content.replace('”','”')
    content = content.replace('“','“')
    content = content.replace('"','"')
    content = content.replace('©','©')
    content = content.replace('®','®')
    content = content.replace(' ',' ')
    content = content.replace('—','—')
    content = content.replace('–','–')
    content = content.replace('‹','‹')
    content = content.replace('›','›')
    content = content.replace('…','…')
    content = content.replace('&','&')
    return content

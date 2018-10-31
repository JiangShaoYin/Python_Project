#! /usr/bin/python3.5
#    coding:utf-8
#	 @file    ExtractTelAndEmail.py
#	 @author  Sean(jiangshaoyin@pku.edu.cn)
#	 @date    2018-10-31 18:01:13
 
 
import pyperclip
import re
                                                #r () () ()有分组的正则表达式，findall将返回字符串元组的列表,[('1','2','3'),('4','5'),('6','7')]
PhoneRegEx = re.compile(r'''(                   #return an object named PhoneRegEx which belongs to class RegEx
                        (\d{3} | \(\d{3}\) )?   #1,区号，\d{3}:长度为3的数字，或者括号内的3个数字\(\d{3}\),\符号转义括号,?匹配字符串短的那个字符
                        (\s | - | \.)?          #2,分隔符，\s通配空字符， \.表示匹配的是字符.而不是通配符.(表示通配除\n以外的所有字符的那个通配符)
                        (\d{3})                 #3,前3个字符
                        (\s | - | \.)           #4,分隔符
                        (\d{4})                 #5,后四个字符
                        (\s*(ext|x|ext.)\s(\d{2,5}))?   #6,分机号，以ext | x | ext.开头,匹配2-5位的数字
                        )''',re.VERBOSE)
EmailRegEx = re.compile(r'''(
                        [a-zA-Z0-9._+%-]+       #用户名,[]内的东西至少出现1次
                        @
                        [a-zA-Z0-9.-]+            #站名
                        (\.[a-zA-Z]{2,4})       #charactors behind the dot
                        )''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for group in PhoneRegEx.findall(text):  #findall返回text中按照PhoneEegEx对象，查找方法的结果列表
    phone_num = '-'.join([group[1], group[3], group[5]])      #以“-”连接字符串 
    if group[8] != '':                  #???
        phone_num += ' x' +group[8]
    matches.append(phone_num)
for group in EmailRegEx.findall(text):
    matches.append(group[0])

#copy result to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('no phone numbers or email addresses found.')


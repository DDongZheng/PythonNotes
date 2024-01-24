#有效的括号——Valid Parentheses
#题号：20
#日期：240124
#关键思路：左括号进栈，搭配右括号出栈，右括号不进栈

"""
我所学到的：
1. 列表作栈
2. 考虑栈的溢出问题
3. 字典
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    访问字典元素
    value_of_key1 = my_dict['key1']
    判断键是否存在
    if 'key1' in my_dict:
"""

class Solution(object):
  def isValid(self,s):
    dic = {'{':'}','[': ']', '(': ')', '?': '?'}
    # 创建字典，用于检查字符串中左右括号是否匹配
    stack = ['?']
    # 列表作栈
    # 如果第一个字符是右括号的话，防止出栈报错
    for c in s:   #遍历字符串
      if c in dic:  #如果进栈的括号是左括号
        stack.append(c) #进栈
      elif dic[stack.pop()] != c: #如果出栈的括号不匹配当前的字符串元素
        return False  #返回False
    return len(stack) == 1


    



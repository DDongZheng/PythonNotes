#有效的括号——Valid Parentheses
#题号：20

Class Solution(Object):
  def isValid(self,s):
    dic = {'{':'}','[': ']', '(': ')', '?': '?'}
    # 创建字典，用于检查字符串中左右括号是否匹配
    stack = ['?']
    # 列表作栈
    # 如果第一个字符是
    for c in s:
      if c in dic:
        stack.append(c)
      elif dic[stack.pop] != c:
        return False
    return len(stack) == 1


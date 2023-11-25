import unittest

# 测试函数
def get_formatted_name(first,last,middle=''):
    '''Generate a neatly formatted full name.'''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

print('Enter q to quit.')
while True:
    first = input('Enter your first name:')
    if first == 'q':
        break
    last = input('Enter your last name:')
    if last == 'q':
        break
    fornatted_name = get_formatted_name(first,last)
    print('Your name:' + fornatted_name)

# 单元测试和测试用例
class NamesTestCase(unittest.TestCase):
    '''测试get_formatted_name()函数'''

    def test_first_last_name(self):
        '''能够正确处理向zhang yiju这样的姓名吗？'''
        fornatted_name = get_formatted_name('zhang','yiju')
        self.assertEqual(fornatted_name,'Zhang Yiju')
    
    def test_first_last_middle_name(self):
        '''处理中间名字'''
        fornatted_name = get_formatted_name('zhang','yiju','da')
        self.assertEqual(fornatted_name,'Zhang Da Yiju')

unittest.main()

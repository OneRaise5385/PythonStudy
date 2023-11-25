# 测试类

# 一个要测试的类
class AnonymousSurvey():
    '''收集匿名调查问卷答案'''

    def __init__(self,question):
        '''存储一个问题，并为存储答案做准备'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_response(self,new_response):
        '''存储单份调查问卷'''
        self.responses.append(new_response)

    def show_results(self):
        '''显示收集到的所有调查问卷'''
        print('Result:')
        for response in self.responses:
            print('-' + response)

# 执行类的程序
question0 = 'Language?'
my_survey0 = AnonymousSurvey(question0)
my_survey0.show_question()
print('Enter q to quit.')
while True:
    response0 = input('Language:')
    if response0 == 'q':
        break
    my_survey0.store_response(response0)
my_survey0.show_results()


# ????????????????????????????????????????????
# 测试AnonymousSurvey类
# import unittest
# class TestAnonmyousSurvey(unittest.TestCase):
#     '''测试AnonymousSurvey类'''

#     def test_store_singel_response(self):
#         '''测试单个答案能够被存储'''
#         question = 'Language?'
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('python')
#         self.assertIn('python',my_survey.responses)

#     def test_store_three_responses(self):
#         '''测试三个答案是否能被妥善地存储'''
#         question = 'Language?'
#         my_survey = AnonymousSurvey(question)
#         responses = ['python','c','java']
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response,my_survey.responses)  
# unittest.main()
# ????????????????????????????????????????????

'''
Define a function that would replace a blank in a string with '%20'
e.g. string is "we are happy", the output is supposed to be "we%20are%20happy"
'''

class Solution:
    #Using the basic function of python
    def replace1(self,string):
        if type(string) != str:
            return ('')
        return string.replace(' ','%20')
    #create a new string to replace
    def replace2(self,string):
        newstr = ''
        if type(string) != str:
            return ('')
        for i in string:

            if i ==' ':
                newstr +='%20'
            else:
                newstr += i
        return (newstr)


    #The method of basic
    def replace3(self,string):
        if type(string) != str or len(string) <= 0 or string == None:
            return ''
        spaceNum = 0
        for i in string:
            if i  == ' ':
                spaceNum += 1

        lenOrig = len(string)
        lenNew = lenOrig + spaceNum*2
        strNew = lenNew * [None]

        indexOrig, indexNew = lenOrig-1,lenNew-1
        while indexNew >=0 and indexNew >= indexOrig:
            if string[indexOrig] == ' ':
                strNew[indexNew-2:indexNew+1] = ['%','2','0']
                indexNew -= 3
                indexOrig -= 1
            else:
                strNew[indexNew] = string[indexOrig]
                indexNew -= 1
                indexOrig -= 1
        return (''.join(strNew))

string = 'I am lucky haha.'
Rep = Solution()
print(Rep.replace1(string))
print(Rep.replace2(string))
print(Rep.replace3(string))
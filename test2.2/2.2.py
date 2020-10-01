#-*- coding: utf-8 -*

number=[2,3,4,5]
print(number[0:2])
#
# year= input('year:')
# month = input('month:')
# day = input('day:')

# month_number= int(month)
# day_number=int(day)
# months=["a","b","c","d","e","f","h"]

# month_name= months[month_number-1]


# print(year + month_name + day)
#


#ucl=input("please type address:")
#domain=ucl[1:5]
#print(domain)

ab=[0,12,3,24]
print(min(ab),max(ab),len(ab))


x=[1,3,5,6,7,9]
x.reverse()
x.sort()
print(x)


y =[3,1,6,3,9,12,32,21]
x= y.sort()
print(x)

z=[3,1,6,3,9,12,32,21]
x=z[:]
x.sort()
print(x)

x=z
x.sort()
print(x)


number=[6,9,3,4]
number.sort()
print(number)

tuple([1,2,3])
tuple('abc')
list((1,2,3))

print((1,2,3))

print('%s plus %s equals %s' %(1,1,2))

print('hexademical number: %x' %42)

print('using str: %s' % 42)

print('using repr: %r' %42)

print('%010.2f' %23)
print('%10.2f' %23)
print('%10f' %23)
print('%.2f' %23)
print('%-10.2f' %23)

header_format= '%-*s %*s'
item_width=10
price_width=10
print( header_format % (item_width,'item',price_width,'price') )

subject= 'python is boring'
print(subject.find('python'))
print(subject.find('is'))


seq=['1','2','3']
sep='+'
print(sep.join(seq))
name='WANGQIRUN'
print(name.lower())

print('this is a test'.replace('is','abc'))

a=[1,2,3,4,5]
a.reverse()

print('abc'.count('a'))
print([1,2,3,4,5,67,32,23].count(1))

from random import choice
x= choice(['hello,world',[1,2,3,'e','e',4]])
print(x.count('e'))

class openobject:
    def set(self):
     self.name=input()

    def getname(self):
        return self.name
    def get2(self):
        self.getname()

o= openobject()
o.set()
print(o.getname())
print(o.get2())


class MemberCounter:
    member=0;
    def get3(self):
        self.member +=1



# issubclass(openobject,)
#isinstance(s,filter)










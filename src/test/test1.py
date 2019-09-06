'''
class A(object):
    i='0'
class B(A):
    pass
class C(A):
    pass
B.i='1'
A.i='2'
print(A.i,B.i,C.i)
'''
arr = [1,2,3,4,5,6]
print(arr[0:1])
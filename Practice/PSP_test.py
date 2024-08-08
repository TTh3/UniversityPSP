def function1():
    global j
    j = 1
    k = 2
    print('j is:', j, 'k is', k)
def function2(j, k):
    j = 8
    k = 7
    print('j is:', j, 'k is', k)
def function3():
    print('j is:', j, 'k is', k)
def function4():
    function3()
    j = 300
j = 'one'
k = 'two'
function1()
print('j is:', j, 'k is', k)
function2(j,k)
print('j is:', j, 'k is', k)
function4()
print('j is:', j, 'k is', k)
k = 'three'
function1()
print('j is:', j, 'k is', k)

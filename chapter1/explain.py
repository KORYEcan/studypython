""" 

모든 프로그래밍은 결국 데이터를 다루는 행위
파이썬의 자료형으로는 정수형 , 실수형, 복소수형 , 문자열, 리스트 , 튜플, 사전등이 있슴



 """


 # 정수형은 정수를 다루는 자료형-> 양의 정수 , 음의 정수 , 0이 포함됨


a= 1000
print (a)

a= -7
print(a)

a= 0 
print(a)

#실수형 (Real Number)은 소수점 아래의 데이터를 포함하는 수 자료형
#파이썬에서는 변수에 소수점 소수는 0을 생략하고 작성할 수 있습니다.을 붙인 수를 대입하면 실수형 변수로 처리
# 소수부가 0이거나, 정수부가 0인 소수는 0을 생략하고 작성할 수 있습니다.


a= 157.93
print(a)

a= -1837.32
print(a)

""" 
지수 표현 방식 
e 나 E를 이용한 지수 표현 방식을 이용

유효숫자e 지수 = 유효숫자 X 10지수
지수 표현 방식은 임의의 큰수를 표현하기 위해 자주 사용
 """
 #1,000,000,000의 지수 표현 방식
a= 1e9
print(a)

#752.5
a= 75.25e1
print(a)

#3.954
a= 3954e-3
print(a)

"""  실수형을 저장하기 위해 4바이트 ,8바이트의 고정된 크기의 메모리를 할당
컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가짐
예를 들어 10진수 체계에서는 0.3과 0.6을 더한 값이 0.9로 정확히 떨어짐
하지만 2진수에서는 0.9를 정확히 표현할 수있는 방법이 없음
그래서 컴퓨터는 최대한 0.9와 가깝게 표현하지만, 미세한 오차가 발생하게 됨 

해결방안-> round()함수를 이용
 """

""" a= 0.3 + 0.6
print(a)

if a== 0.9:
    print(True)
else:
    print(False)

a= 0.3 + 0.6
print(a) """

############################ round() 함수를 사용해서 해결하기

if round(a,4) == 0.9 :
    print(True)
else:
    print(False)


""" 
      파이썬에서는 나누기 연산자(/)는 나눠진 결과를 실수형으로 반환
      다양한 로직을 설계할 때 나머지연산자(%)를 이용해야 할때가 많음
      몫을 얻기위해 몫 연산자(//)를 사용
      이외에도 거듭 제곱연산자(**)를 비롯해 다양한 연산자들이 존재
"""

    
z= 7
x= 3
#나눠진 결과를 실수형으로 반환 (/)
print(z/x)
#나머지 연산자(%)
print(z%x)
#몫을 얻기위한 연산자 (//)
print(z//x)

##거듭 연산자

a= 5
b= 3
#거듭 제곱
print(a **b)
#제곱근
print(a ** 0.5)


""" 
여러개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
사용자 입장에서 C나 자바에서의 배열(Array)의 기능 및 연결리스트와 유사한 기능 
리스트 대신에 배열 혹은 테이블이라고 부르기도 함

리스트는 대괄호([])안에 원소를 넣어 초기화하여, 쉼표(,)로 원소를 구분
비어있는 리스트를 선언하고자 할 때는 list() 혹은 간단히 []을 이용할 수 있슴
리스트의 원소에 접근할 때는 인덱스(Index)값을 괄호에 넣음
"""
#직접 데이터를 넣어 초기화
a= [1,2,3,4,5,6,7,8,9]
print(a)

#네 번쨰 원소만 출력
print(a[3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n= 10
a=[4]* n
print(a)

#인덱스 값을 입력하여 리스트의 특정한 원소에 접근하는 것을 인덱싱(Indexing)
#음의 정수를 넣으면 원소를 거꾸로 탐색하게 됨

a=[1,2,3,4,5,6,7,8,9,10]
print(a[7])
#리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할떄는 슬라이싱(Slicing)을 이용
#대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 끝 인덱스를 설정
# 끝 인덱스는 실제 인덱스보다 1을 더크게 설정 
print(a[-10])
print(a[1:4])

""" #리스트 컴프리핸션
초기화하는 방법 중 하나 , 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화
2차원 리스트를 초기화할때 효과적으로 사용
특히 N X M 크기의 2차원 리스트를 한 번에 초기화 할 때 매우 유용
ex) array =[[0] * m for_ in range(n)] -> 좋은 코드
다음과 같이 2차원 리스트를 초기화하면 예기치 않은 결과를 나올수도 있음
위코드는 전체 리스트안에 포함된 각 리스트가 모두 같은 객체로 인식 
ex) array= [[0] * m] *n -> 잘못된 코드 
"""
array = [i for i in range(10)]
print(array)
array =[ i for i in range(4)]
print(array)
#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range (20) if i% 2== 1]
print(array)
# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트 1*1, 2*2 , 3*3, 4*4
array= [i + i for i in range(1,10)] 
print(array)


# 코드 1: 리스트 컴프리핸션
array= [i + i for i in range(1,10)] 
print(array)

#코드 2: 일반적인 코드
array=[]
for i in range(20):
    if i % 2 == 1:
     array.append(i)
     
print(array)



# N X M 크기의 2차원 리스트 초기화-> 좋은 예시
n= 4
m= 3
array =[[0] * m for _ in range(n)]
print(array)

# 잘못된 방법
n= 4
m= 3
array= [[0]* m ]* n
print(array)
array[1][1] =5
print(array)

""" 
언더바는 언제 사용하나요?
파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용
"""
#코드 1ㅣ 1부터 9까지의 자연수를 더하기
summary= 0
for i in range(1,10):
    summary+=i
print(summary)

#코드 2ㅣ "Hello World"를 5번 출력하기
for _ in range(5):
    print("hello world")
    
    """ 
    append()->변수명.append() -> 리스트에 원소를 하나 삽입할때
    sort()->변수명.sort()-> -> 기본 정렬 기능으로 오름차순 정렬
    reverse()->변수명.rerverse()  -> 리스트의 원소 순서를 모두 뒤집어 놓는다
    insert()-> insert(삽입할 위치 인덱스, 삽입할 값) -> 특정한 인덱스 위치에 원소를 삽입할 때 사용
    count()->  변수명.count(특정 값)->리스트에서 특정한 값을 가지는 데이터의개수를 셀 때 사용
    remove()-> 변수명.remover(특정 값)->특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러개면 하나만 제거함
    """
    
a =[ 1,5,12]
print("기본 리스트:", a)
a.append(2)
print("삽입:",a)

#기본 오름차순 정렬
a.sort()
print("오름차순 정렬:",a)

#내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬:",a)

#리스트 원소 뒤집기
a=[4,3,2,1]
a.reverse()
print("원소 뒤집기:",a )

#특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3추가 :",a)

#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수:",a.count(3))

#특정 값 데이터 삭제 
a.remove(1)
print("값 1인 데이터 삭제:",a)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a =[1,2,3,4,5,5,5]
remove_set={3,5} #집합 자료형 

#remove_list에 포함되지 않은 값만을 저장
result =[i for i in a if i not in remove_set]
print(result)



""" 
문자열 자료형
초기화할 때는 큰따옴표(") , 작은 따옴표(')
큰따옴표나 작은 따옴표가 포함되어야 하는 경우가 있슴
전체 문자열을 큰따옴표로 구성하는 경우, 내부적으로 작은 따옴표를 포함O
전체 문자열을 작은 따옴표로 구성하는 경우, 내부적으로 큰 따옴표를 포함O
백슬래쉬(\)를 사용하면, 큰따옴표나 작은 따옴표를 원하는 만큼 포함시킬수 있음
"""

data= 'Hello World'
print(data)

data = "DOn't you know \"Python\"?"
print(data)

""" 
문자열 연산
덧셈(+) 이용하면 더해져서 연결 됨
정수와 곱하는 경우, 문자열이 그 값만큼 여러 번 더해짐
문자열에 대해서도 마찬가지로 인덱싱과 슬라이싱을 이용가능
다만 문자열은 특정 인덱스의 값을 변경X
"""

""" 
튜플 자료형
리스트와 유사하지만 다음과 같은 문법적 차이가 있음
튜플은 한번 선언된 값을 변경X
리스트는 대괄호([])를 이용하지만, 튜플은 (()) 를 이용함
리스트에 비해 상대적으로 공간 효율적

장점:
서로 다른 성질의 데이터를 묶어서 관리해야 할 때
-> 최단 경로 알고리즘에서는 (비용,노드 번호)의 형태로 튜플 자료형을 자주 사용
데이터의 나열을 해싱의 키 값으로 사용할떄
튜플은 변경이 불가능, 리스트와 다르게 키 값으로 사용 될수 있음
리스트 보다 메모리를 효율적으로 사용해야 할때 
"""
a= (1,2,3,4,5,6,7,8,9)

print(a[3])

#튜플 잘못된 사용예제
""" 
Traceback (most recent call last):
  File "c:\pythonpractice\chapter1\explain.py", line 288, in <module>
    a[2]=7
    ~^^^
TypeError: 'tuple' object does not support item assignment"""
""" a= (1,2,3,4)
print(a)
a[2]=7 """


""" 
사전 자료형
키와 값의 쌍을 데이터로 가지는 자료형
앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됨
원하는 변경 불가능 자료형을 키로 사용 할수 있음
해시테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리

사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원함
키데이터만 뽑아서 리스트로 이용할때는 keys()함수를 사용
값데이터만 뽑아서 리스트로 이용할때는 values()함수를 사용
"""
data = dict()
data['사과']= 'Apple'
data['바나나']= 'banana'
data['코코넛']= 'coconut'
print(data)

if '사과' in data:
    print("'사과'를 가지는 데이터가 존재함")
    
print(data.keys())
print(data.values())


"""
집합자료형
 중복 허용X
순서X
리스트 혹은 문자열을 이용해서 초기화,set()함수를 이용
중괄홀({})안에 각 원소를 콤마(,)를 기준으로 구분하여 삽입함으로써 초기화할 수있음
데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할수 있음


집합 자료형의 연산
합집합: 집합 A에 속하거나 B에 속하는 원소로 이루어진 집합(A U B)
교집합: 집합 A에도 속하고 B에도 속하는 원소로 이루어진 집합 (A n B)
차집합: 집합 A의 원소 중에서 B에 속하지 않는 원소들로 이루어진 집합 (A - B)
"""
#초기화 방법1
data= set([1,1,2,3,4,4,5])
print(data)

#초기화 방법2
data= {1,1,2,3,4,4,5}
print(data)


# 집합 자료형의 연산
a= set([1,2,3,4,5])
b= set([3,4,5,6,7])

#합집합
print("합집합:",a|b)

#교집합
print("교집합:",a&b)

#차집합
print("차집합:",a-b)

data = set([1,2,3])
print(data)

#새로운 원소 추가 
data.add(4)
print(data)

#새로운 원소 여러 개 추가
data.update([5,6])
print(data)

#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

""" 
리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있습니다.
사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없습니다.
 사전의 키 혹은 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회함
"""


""" 
자주 사용되는 표준 입력 방법
input() 한줄의 문자열을 입력 받는 함수
map() 리스트의 모든 원소에 각각 특정한 함수를 적용할 떄 사용

예시) 공백을 기준으로 구분된 데이터를 입력받을 때는 다음과 같이 사용합니다
list(map(int, input().split()))
예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과같이 사용합니다
a,b,c= map(int, input().split())
"""
#데이터의 개수 입력
# n= int(input())

#각 데이터를 공백을 기준으로 구분하여 입력
# data =list(map(int, input().split()))

# data.sort(reverse=True)
# print(data)


# a, b, c 를 공백 기준으로 구분하여 입력
# a,b,c= map(int, input().split())
# print(a,b,c)



""" 
빠르게 입력 받기
사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있슴
파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용함
단, 입력 후 엔터(Enter)가 줄바꿈 기호로 입력되므로 rstrip() 메서드를 함꼐 사용함


파이썬에서 기본 출력은 print()함수를 이용
각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분하여 출력할수 있습니다
print()는 기본적으로 출력 이후에 줄 바꿈을 수행
줄 바꿈을 원치 않는 경우 'end'속성을 이용할수 있습니다.
"""

# import sys
# data = sys.stdin.readline().rstrip()
# print(data)



#출력할 변수들
# a = 1 
# b = 2 
# print (a,b)
# print(7,end=" ")
# print(8,end=" ")

# #출력할 변수
# answer = 7
# print("정답은 " + str(answer)+"입니다.")



#f-string 파이썬 3.6부터 사용 가능, 문자열 앞에 접두사 'f'를 붙여 사용함
#중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있습니다.

# answer= 7
# print(f"정답은 {answer}입니다.")


x= 45
if x >= 10:
    print("x>=10")
if x >= 0:
    print("X>=0")
if x >=30:
    print("x>= 30")
        
        
        
score= 65

if score >=70:
    print("성적이 70점 이상입니다.")
else:
    print("성점이 70점이하 입니다.")
    
    

# score = 85

# if score >= 90:
#     print("학점: A")
# elif score >= 80:
#     print("학점 : B")
# elif score >= 70:
#     print("학점 : C")
# else:
#     print("학점: F")    
    
    
    
    
a = 15

if a <= 20 and a >= 0:
	  print("Yes")
   
   
a= 50 
if a >=30:
     pass
else:
     print("a< 30")
     
     
     
i = 1
result= 0
# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행 
while i <= 9 :
    result+= i
    i +=1
    
print(result)






# array= [9,8,7,6,5]

# for x in array:
#     print(x)
    
#     result = 0 
    
#i 는 1 부터 9까지의 모든 값을 순회
for i in range(1,10):
    result += i
    
print(result)


result= 0 
for i in range(1,10):
    if i% 2==0:
        continue
    result += i
print(result)


i= 1
while True:
    print("현재 i의 값:",i)
    if i == 5:
        break
    i+=1
    
 
 
 # 특정 번호의 학생은 제외하기
scores= [90,85,77,65,97]
cheating_student_list={2,4}  #특정 번호의 학생은 제외함 

for i in range(5):
    if i + 1 in cheating_student_list: #인덱스값은 0부터 시작하니깐 +1 해줘서 몇번 학생인지 나타내준다.
        continue
    if scores[i] >= 80:
        print(i+1,"번 학생은 합격입니다.")   #인덱스값은 0부터 시작하니깐 +1 해줘서 몇번 학생인지 나타내준다.
    
    
    #구구단 
for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
print()

def add( a,b ):
    return a+ b

print(add(1,2))


a= 0

def func():
    global a
    a +=1
    
for i in range(10):
    func()

print(a)



def operator(a,b):
    add_var= a+b
    subtract_var=a-b
    multiply_var=a*b
    divide_var=a/b
    return add_var,subtract_var,multiply_var,divide_var

a,b,c,d = operator(7,3)
print(a,b,c,d)



def add(a,b):
    return a+b
#일반적인 add() 메서드 사용
print(add(3,7))

#람다 표현식으로 구현한 add()메서드
print((lambda a, b: a+b)(3,7))


#람다 표현식-> 내장 함수에서 자주 사용되는 람다 함수 
array=[('홍길동',50),('이순신',32),('아무개',74)]


def my_key(x):
    return x[1]

print(sorted(array,key=my_key))
print(sorted(array,key=lambda x: x[1]))

#여러개의 리스트에 적용
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
result= map(lambda a,b : a+b , list1, list2)
print(list(result))


#sum
result=sum([1,2,3,4,5])
print(result)

#min() max()
min_result= min(7,3,5,2)
max_result= max(7,3,5,2)
print(min_result,max_result)

#eval()
result = eval("(3+5)*7")
print(result)

#sorted()
result = sorted([9,1,8,5,4])
reverse_result=sorted([9,1,8,5,4],reverse=True)
print(result)
print(reverse_result)
#sorted() with key
array=[('홍길동',35),('이순신',75),('아무개',50)]
result= sorted(array,key=lambda x: x[1], reverse=True)
print(result)

#조합-> 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는것 
 #-> 순서를 고려하지 않고 두개를 뽑는 경우 : 'AB' 'AC' 'BC'
 
from itertools import combinations
data=['A','B','C']
result= list(combinations(data,2))
print(result)


#중복 순열과 중복 조합
from itertools import product
data=['A','B','C']  #데이터 준비
result= list(product(data, repeat=2)) #2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)


from itertools import combinations_with_replacement

data= ['A','B','C']

result= list(combinations_with_replacement(data,2))
print(result)


from  collections import Counter
counter =Counter(['red','blue','red','green','blue','blue'])

print(counter['blue']) #'blue'가 등장한 횟수 출력
print(counter['green']) #'green'이 등장한 횟수출력
print(dict(counter))  #사전 자료형으로 반환 

import math
#최소 공배수(LCM)를 구하는 함수
def lcm(a,b):
    return a * b // math.gcd (a,b)

a= 21
b= 14

print(math.gcd(21,14)) #최대 공약수 (GCD)계산 
print(lcm(21,14)) #최소 공배수(LCM)계산 
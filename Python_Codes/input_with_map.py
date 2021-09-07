
try : 

    # a, b, c를 공백으로 구분하여 입력받기
    print("3개의 숫자를 입력하세요")
    a, b, c = map(int, input().split())

    mylist = a, b, c
    mylist = list(mylist)
    mylist.sort()
    print(mylist)

    # N개의 수를 공백으로 구분하여 입력받기
    print("원하는 개수의 단어를 입력하세요")
    arr = list(map(str, input().split()))

    print("*** 1번째 입력 결과 ***")
    print("a : {0}, b: {1}, c : {2}".format(a, b, c))
    print("*** 2번째 입력 결과 ***")
    print("arr : {0}".format(arr))
except : 
    print("잘못된 입력입니다.")
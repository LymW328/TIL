#여러사람의 혈액형에 대한 정보가 담긴 list를 전달받아 key는 혈액형 종류,  value는 사람 수인 dictionary를 만드시오.
# blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
# a = (blood_types.count("A"))
# ab = (blood_types.count("AB"))
# o = (blood_types.count("O"))
# b = (blood_types.count("B"))
# res = dict(A = a, B = b, AB = b, O = o)
# print(res)


def pre():
    blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
    #딕셔너리를 활용하는 방법
    count_dict = {'A' : 0,'B' : 0,'AB' : 0,'O' : 0}
    for blood in blood_types:
        count_dict[blood] += 1
    print(count_dict)

pre()
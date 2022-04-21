def func(referenc_types):
    if type(referenc_types) == Node:
        referenc_types.x = "변한다."
    elif type(referenc_types) == list:
        referenc_types[0] = "변한다."


class Node:
    # 생성자
    def __init__(self):
        self.x = 10

    # __str__ 은 str(instance) 시 반환되는 값
    # print 는 자동으로 str(instance)를 해주기 때문에
    # 아래와 같은 사용이 가능하다.
    def __str__(self):
        return str(self.x)

node_a = Node()
list_b = ["bye bye"]
print(node_a)
print(list_b)
print("=====Before Func=====")
func(node_a)
func(list_b)
print("======After Func=====")
print(node_a)
print(list_b)

def func(primitive_variables):
    primitive_variables = "변하지 않는다."


int_a = 10
str_b = "hello"
float_c = 10.123
bool_d = False
complex_e = 1 + 3j
print(int_a)
print(str_b)
print(float_c)
print(bool_d)
print(complex_e)
print("=====Before Func=====")
func(int_a)
func(str_b)
func(float_c)
func(bool_d)
func(complex_e)
print("======After Func=====")
print(int_a)
print(str_b)
print(float_c)
print(bool_d)
print(complex_e)


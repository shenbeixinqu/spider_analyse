cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data = [123, 153, 89, 107, 98, 23]


res = [list(z) for z in zip(cate, data)]
print('res', res)
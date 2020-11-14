object1 = {"x":{"y":{"z":"a"}}}
def get_all_values(object1):
    for key, value in object1.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(value)
get_all_values(object1)
type_error_list=[]
try:
    print("Doing some stuff ...")
    # ooops!
    print(1 + '1')
    print(x)

except TypeError as t:
    type_error_list.append(t)

if len(type_error_list) > 0:
    print('The following Type Errors occured:')
    for error in type_error_list:
        print(error)



try:
    print("Doing some stuff ...")
    # ooops!
    print(x)

except NameError as n:
    print('Name Error found:', str(n))




# except Exception as e:
#     print(str(e))
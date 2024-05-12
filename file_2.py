list1 = [1,2,['kiran',4,('d','er',[90,20])], {'car':'ducati','surname':'jagtap'}, 'apple']

def flatten_list(l1):
    output = []
    
    def recursive_func(l1):
        for i in l1:
            if isinstance(i,list) or isinstance(i,tuple) or isinstance(i,set):
                recursive_func(i)
            elif isinstance(i,dict):
                recursive_func(i.items())
            else:
                output.append(i)
    recursive_func(l1)
    return output

print(flatten_list(list1))
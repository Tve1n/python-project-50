from gendiff.parser import parse_data_from_file

def generate_diff(file1, file2):
    obj_f1 = parse_data_from_file(file1)
    obj_f2 = parse_data_from_file(file2)
    result_list = ['{\n']
    list_of_keys = sorted(list(set(list(obj_f1) + list(obj_f2))))
    for key in list_of_keys:
        if (key in obj_f1) and (key not in obj_f2):
            result_list.append(f'  - {key}: {obj_f1[key]}\n')
        elif (key in obj_f1) and (key in obj_f2):
            if obj_f1[key] == obj_f2[key]:
                result_list.append(f'    {key}: {obj_f1[key]}\n')
            else:
                result_list.append(f'  - {key}: {obj_f1[key]}\n')
                result_list.append(f'  + {key}: {obj_f2 [key]}\n')
        else:
            result_list.append(f'  + {key}: {obj_f2 [key]}\n')
    result_list.append('}')

    return ''.join(result_list)

#print(generate_diff('tests/fixtures/file1.json', ''tests/fixtures/file2.json'))
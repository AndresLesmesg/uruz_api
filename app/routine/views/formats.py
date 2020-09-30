
def request_null():
    return 'request null'


def request_successful():
    return 'successful transaction'


def output_format(data):
    data = clear_query(data)
    item = data.split(',')
    result = {}
    for i in item:
        value = i.split(':')
        result[value[0]] = value[1]

    return result


def output_format_all(data):
    data = clear_query(data)
    item_list = data.split(', ')
    result = {}
    dict_list = []

    for x in item_list:
        x = clear_query(x)
        item = x.split(',')

        for i in item:
            value = i.split(':')
            result[value[0]] = value[1]
        dict_list.append(dict(result))

    return dict_list


def clear_query(data):
    data = str(data)
    if data[0] == '[' or data[0] == '(':
        data = data.replace(data[0], '')
        data = data.replace(data[len(data)-1], '')

    return data

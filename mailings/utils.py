def minute_in_hour(data):
    data = [int(el) for el in data.split(':')]
    data = data[0] * 60 + data[1]

    return data

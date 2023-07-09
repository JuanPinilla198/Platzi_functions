def get_population(country):
    keys = country.keys()
    values = country.values()
    return  keys, values

def population_by_country(data, country):
    data_list = []
    headers = []
    values= []
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    if result == []:
        raise Exception('Country not found')
    for dict_data in result:
        for keys, value in dict_data.items():
            headers.append(keys)
            values.append(value)     
    labels = list(name.replace(' Population', '') for name in headers[5:13])
    values = values[5:13]
    iterable = zip(labels, values)
    country_dict = {key: int(value) for key, value in iterable}
    data_list.append(country_dict)
    return data_list

def get_mean_population(data, continent):
    data = list(filter(lambda item: item['Continent'] == continent, data))
    if data == []:
        raise Exception('Continent not found')
    labels = list(map(lambda item: item['Country/Territory'], data))
    values = list(map(lambda item: item['World Population Percentage'], data))

    return labels, values
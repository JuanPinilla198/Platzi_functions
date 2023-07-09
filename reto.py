import csv

def read_cvs(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      if row[2] == 'Colombia':
        labels = list(name.replace(' Population', '') for name in header[5:12])
        values = row[5:12]
        iterable = zip(labels, values)
        country_dict = {key: value for key, value in iterable}
        data.append(country_dict)
  return data


if __name__ == '__main__':
  data = read_cvs('./csv/data.csv')
  print(data)
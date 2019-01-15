def get_data(filename):
  info = {}
  key = ''
  with open(filename, 'r') as file:
    document = file.readlines()
    for line, i in zip(document, range(0, len(document)):
      if i % 2 == 0:
        key = line
        info[key] = []
      else:
        for data in line.split():
          info[key].append(data)



names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


for index, (name, country) in enumerate(zip(names, countries),1):
    print(f'{index}. {name:10} {country}')

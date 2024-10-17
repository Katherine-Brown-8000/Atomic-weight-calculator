import json
import requests

url = "https://raw.githubusercontent.com/Katherine-Brown-8000/Computational-Chemistry/refs/heads/main/Atomic_mass_reformat.json"
response = requests.get(url)

if response.status_code == 200:
    atomic_mass = json.loads(response.text)
else:
    print('Failed to retrieve the data.')

# enter your total compounds here
total = 0
while True:
    element = input("enter the abbreviation of your element, type done when finished: ").strip()
    if element.lower() == 'done':
        break

    count = input(f"enter count for {element}: ").strip()

    try:
        count = int(count)
        mass = atomic_mass.get(element)
        if mass is not None:
            total += mass * count
        else:
            print(f"Error: atomic mass for {element} not found")
    except ValueError:
        print('no')

print(f"The combined atomic weight is {total}")

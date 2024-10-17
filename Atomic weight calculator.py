import json
import requests

url = "https://raw.githubusercontent.com/Katherine-Brown-8000/Molarity-Calculator/refs/heads/main/Atomic_Mass_Dictionary.json"
response = requests.get(url)

if response.status_code == 200:
    atomic_mass = json.loads(response.text)
else:
    print('Failed to retrieve the data.')

# enter your total compounds here
total = 0
while True:
    compound = input("enter the abbreviation of your compounds, type done when finished: ").strip()
    if compound.lower() == 'done':
        break

    count = input(f"enter count for {compound}: ").strip()

    try:
        count = int(count)
        mass = atomic_mass.get(compound)
        if mass is not None:
            total += mass * count
        else:
            print(f"Error: atomic mass for {compound} not found")
    except ValueError:
        print('no')

print(f"The combined atomic weight is {total}")

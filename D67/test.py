try:
    response = requests.get(varOcg)
    response.raise_for_status()
    data = response.json()['data']
except requests.RequestException as e:

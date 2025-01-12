import requests


def get_artworks_by_object_numbers(object_numbers: list[str]):
    """
    Fetch information about multiple artworks from the SMK API using their
    object numbers.

    Args:
        object_numbers (list of str): A list of unique object numbers of the artworks.

    Returns:
        dict: JSON response from the API containing the artworks data.
    """
    base_url = 'https://api.smk.dk/api/v1/art/'
    params = [('object_number', obj_num) for obj_num in object_numbers]
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None

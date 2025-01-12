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


def get_artworks_by_search(search_words: list[str], creator_nationality: str = None):
    """
    Fetch information about artworks from the SMK API using search words.

    Args:
        search_words (list of str): A list of keywords to search for in the artworks.
        creator_nationality: The nationality of the artist (In Danish)
    Returns:
        dict: JSON response from the API containing the artworks data.
    """
    base_url = 'https://api.smk.dk/api/v1/art/search/'
    if search_words:
        search_query = (
            f"[{', '.join(search_words)}]"  # Format search words as a list in the query
        )
    else:
        search_query = '*'
    filters = '[has_image:true],[object_names:maleri],[public_domain:true]'
    if creator_nationality:
        filters += f'[creator_nationality:{creator_nationality}]'
    params = {
        'keys': search_query,  # Keywords for search
        'fields': 'titles',  # Fields to return in the response
        'filters': filters,  # Apply filters
        'offset': 0,  # Start position for results
        'rows': 30,  # Number of results to return
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None

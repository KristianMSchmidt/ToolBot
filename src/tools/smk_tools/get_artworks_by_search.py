import requests
from urllib.parse import unquote


def get_artworks_by_search(
    search_words: list[str] = '*', creator_nationality: str = None
):
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
        search_query = f"[{', '.join(search_words)}]"
    else:
        search_query = '*'
    filters = '[has_image:true],[object_names:maleri]'
    if creator_nationality:
        filters += f',[creator_nationality:{creator_nationality}]'
    params = {
        'keys': search_query,  # Keywords for search
        'fields': 'titles',  # Fields to return in the response
        'filters': filters,  # Apply filters
        'offset': 0,  # Start position for results
        'rows': 30,  # Number of results to return
    }

    # Construct the full URL for printing
    full_url = requests.Request('GET', base_url, params=params).prepare().url
    readable_url = unquote(full_url)  # Decode the URL for readability
    print("Requesting data from the following URL:")
    print(readable_url)
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None

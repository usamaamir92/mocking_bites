from lib.cat_facts import *
from unittest.mock import *

def test_cat_facts():
    """mock_fact = Mock()
    response_mock = Mock()
    mock_fact.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"In the 1750s, Europeans introduced cats into the Americas to control pests."}
"""

    mock_fact = Mock()
    mock_fact.get.return_value.json.return_value = {"fact":"In the 1750s, Europeans introduced cats into the Americas to control pests."}

    cat_fact = CatFacts(mock_fact)
    assert cat_fact.provide() == "Cat fact: In the 1750s, Europeans introduced cats into the Americas to control pests."
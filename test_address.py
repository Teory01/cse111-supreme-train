import pytest
from address import extract_city, extract_state, extract_zipcode

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("1600 Pennsylvania Ave NW, Washington, DC 20500") == "Washington"
    assert extract_city("742 Evergreen Terrace, Springfield, IL 62704") == "Springfield"

def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("1600 Pennsylvania Ave NW, Washington, DC 20500") == "DC"
    assert extract_state("742 Evergreen Terrace, Springfield, IL 62704") == "IL"

def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("1600 Pennsylvania Ave NW, Washington, DC 20500") == "20500"
    assert extract_zipcode("742 Evergreen Terrace, Springfield, IL 62704") == "62704"

if __name__ == "__main__":
    pytest.main()

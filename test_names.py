from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Test the make_full_name function with different name cases."""
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Anna", "O'Connor") == "O'Connor; Anna"
    assert make_full_name("Li", "Zhang") == "Zhang; Li"
    assert make_full_name("Jean-Claude", "Van Damme") == "Van Damme; Jean-Claude"
    assert make_full_name("A", "B") == "B; A"  # Short names


def test_extract_family_name():
    """Test the extract_family_name function with different name cases."""
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("O'Connor; Anna") == "O'Connor"
    assert extract_family_name("Zhang; Li") == "Zhang"
    assert extract_family_name("Van Damme; Jean-Claude") == "Van Damme"
    assert extract_family_name("B; A") == "B"  # Short names


def test_extract_given_name():
    """Test the extract_given_name function with different name cases."""
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("O'Connor; Anna") == "Anna"
    assert extract_given_name("Zhang; Li") == "Li"
    assert extract_given_name("Van Damme; Jean-Claude") == "Jean-Claude"
    assert extract_given_name("B; A") == "A"  # Short names


# Call pytest to run the test functions
pytest.main(["-v", "--tb=line", "-rN", __file__])
# pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])


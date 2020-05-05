import pytest
import requests

def test_basic_path():
	r = requests.get("http://localhost:5000/")
	assert r.status_code == '200'

def test_data_to_path():
	r = requests.get("http://localhost:5000/data_to")
	assert r.status_code == '200'	
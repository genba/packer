import pytest
from .app import TestPacker

class TestSimple(object):

	def setup(self):
		TestPacker.install()

	def test_runs(self):
		"""Test that the app fails if started without being installed."""
		TestPacker()

	def test_list_runs(self):
		"""Test whether list runs."""
		p = TestPacker()
		p.list()

	def test_list(self):
		"""Test initial  state."""
		p = TestPacker()
		pkgs = p.list()
		assert isinstance(pkgs, list)

	def test_search_runs(self):
		"""Test whether search runs."""
		p = TestPacker()
		p.search('testing')

	def test_search(self):
		p = TestPacker()
		resp = p.search('testing')
		assert resp.status_code, 200

	def teardown(self):
		TestPacker.uninstall()

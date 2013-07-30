import pytest
from .app import TestPacker

class TestNewInstall(object):

	def test_fails_on_uninstalled_start(self):
		"""Test that the app fails if started without being installed."""
		with pytest.raises(RuntimeError):
			TestPacker()
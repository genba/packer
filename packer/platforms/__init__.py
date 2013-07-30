import platform

try:
	from .windows import WindowsPlatform
except ImportError:
	pass
try:
	from .linux import LinuxPlatform
except ImportError:
	pass


def get_platform():
	"""Detect and instantiate an instance of the underlying platform"""
	# Detect
	platform_str = platform.system()
	print 'Platform detected: {}'.format(platform_str)
	# Instantiate
	if platform_str == 'Windows':
		return WindowsPlatform()
	elif platform_str == 'Linux':
		return LinuxPlatform()
	else:
		raise NotImplementedError('This platform is not yet supported')
		


# Set up correct backend on first import
PAL = get_platform()
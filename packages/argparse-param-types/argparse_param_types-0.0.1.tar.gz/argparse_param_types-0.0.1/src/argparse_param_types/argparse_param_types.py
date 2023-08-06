import logging
import argparse

logger = logging.getLogger(__name__)

def file_type(val, message="Provided file does not exist."):
	""""Argparse type checking that the parameter is an existing file on the filesystem"""
	from os import path
	if path.isfile(val):
		return val
	else:
		logger.error(message)
		raise argparse.ArgumentTypeError(message)

def directory_type(val):
	""""Argparse type checking that the parameter is an existing directory on the filesystem"""
	from os import path
	if path.isdir(val):
		return val
	else:
		logger.error("Provided directory does not exist.")
		raise argparse.ArgumentTypeError("Provided directory does not exist.")

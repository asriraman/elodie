"""
Settings used by Elodie.
"""

from os import path

#: If True, debug messages will be printed.
debug = False

#: Directory in which to store Elodie settings.
application_directory = '{}/.elodie'.format(path.expanduser('~'))

#: File in which to store details about media Elodie has seen.
hash_db = '{}/hash.json'.format(application_directory)

#: File in which to store geolocation details about media Elodie has seen.
location_db = '{}/location.json'.format(application_directory)

#: Elodie installation directory.
script_directory = path.dirname(path.dirname(path.abspath(__file__)))

#: Path to Elodie's ExifTool config file.
exiftool_config = path.join(script_directory, 'configs', 'ExifTool_config')

#: Accepted language in responses from MapQuest
accepted_language = 'en'

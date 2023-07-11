# Leaf Password Generator, a command line utility to generate passwords
# Copyright (C) 2023  Sage I. Hendricks
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import secrets      # secure random
import string       # alphabet string 
import sys          # console arguements
import re           # regex, for processing console args


# get settings from console arguements 
def get_settings (argv):

	# local function declarations 
	# split each arguement fitting format "[string]=[string]" into a key value pair	
	def split_into_pairs (argv):
		# regex script
		rgx_get_pairs = re.compile (r"^([a-zA-Z]+)=([a-zA-Z0-9]+)$")
		# hashtable of arguements keyvaluepairs
		# loops through each element in argv, "... for arguement in argv ... "
		# loop through matches if any are found, "... for m in (rgx_get_pairs.match (arguement) ... ) if m"
		# for each match add a keyValuePair, "m.group (1): m.group (2) ..."
		hashtable = {m.group (1): m.group (2) for m in (rgx_get_pairs.match (arguement) for arguement in argv) if m}

		return hashtable 

	
	# return value if pair exists in proper format, or default_value if not	
	def get_value_bool (table, key, default_value):
		# return value if key is in table, AND value is either true or false
		if key in table and (table[key].lower() == 'true' or table[key].lower() == 'false'):
			return table[key].lower()
		# otherwise return default value	
		return default_value
	
	
	# return value if pair exists in proper format, or default_value if not
	def get_value_int (table, key, default_value):
		# return value if key is in tale, AND value is all digits
		if key in table and (table[key].isdigit()):
			return table[key]
		# otherwise return default value
		return default_value


	# default value declarations
	# integer based 
	default_length  = "16"
	default_count   = "1"
	# boolean based 
	default_upper   = "false"
	default_lower   = "false"
	default_numeric = "false"
	default_special = "false"

	# first get key value pairs
	arguement_pairs = split_into_pairs (argv)
	
	# then get settings values' using get_value_*
	length  = get_value_int  (arguement_pairs, "length",  default_length)
	count   = get_value_int  (arguement_pairs, "count",   default_count)
	upper   = get_value_bool (arguement_pairs, "upper",   default_upper)
	lower   = get_value_bool (arguement_pairs, "lower",   default_lower)
	numeric = get_value_bool (arguement_pairs, "numeric",     default_numeric)
	special = get_value_bool (arguement_pairs, "special", default_special)

	# return settings 	
	return (length, count, upper, lower, numeric, special)


# generate the string used by generate
def generate_alphabet_string (upper, lower, numeric, special):
	alphabet = ""

	# if upper is true, add uppercase letters to string	
	if (upper == "true"):
		alphabet += string.ascii_uppercase
	
	# if lower is true, add lowercase letters to string	
	if (lower == "true"):
		alphabet += string.ascii_lowercase

	# if numeric is true, add numbers to string	
	if (numeric == "true"):
		alphabet += string.digits

	# if special is true, add special character to string	
	if (special == "true"):
		alphabet += string.punctuation

	# return the concatenated string 
	return alphabet


# generate a password of "length" long, from the string "alphabet"
def generate (length, alphabet):
	# get length number of characters for alphabet, randomly, in a char[]
	# then join them together into a string
	return ''.join(secrets.choice(alphabet) for i in range (length))	


# print each element in pass_list to terminal, on new line
def print_result (pass_list):
	for password in pass_list:
		print ("%s" % password)


# main execution line, take console arguements 
def main (argv):
	# first get commandline arguements from "get_settings"
	pass_length, pass_count, upper, lower, numeric, special = get_settings (argv)
	
	# next, generate the string of character we want in the password
	alphabet = generate_alphabet_string (upper, lower, numeric, special)
	# if alphabet is empty string, exit without trying to generate anything 	
	if (alphabet == ""):
		return	

	# generate "pass_count" num of passwords
	passwords = [generate (int (pass_length), alphabet) for _i in range (int (pass_count))]

	# print passwords '\n' terminated to terminal
	print_result (passwords)


# run main function
if __name__ == "__main__":
	main (sys.argv[1:])     # run main passing all arguements, except for the file name
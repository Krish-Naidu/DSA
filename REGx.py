# regex for validating a email adress 
import re


def is_valid_email(email):
	# This regex pattern matches most valid email addresses.
	# It checks for:
	# - Allowed characters before the '@' (letters, numbers, _, ., +, -)
	# - An '@' symbol
	# - Allowed characters for the domain name
	# - A dot (.) followed by domain extension
	# Updated pattern: only allows emails ending with .com
	pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com$"
	return re.match(pattern, email) is not None

	# Returns True if the email matches the pattern, False otherwise

# Example usage:
test_email = "example@email.dfg"
# print(is_valid_email(test_email))  # Output: True if valid, False otherwise
test_email = "example@email.com"
# print(is_valid_email(test_email))  # True if valid, False otherwise



import re
# Import the regular expressions module

def is_valid_credit_card(card_number):
	# Define regex patterns for each card company
	patterns = {
		"Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",  # 13 or 16 digits, starts with 4
		"MasterCard": r"^5[1-5][0-9]{14}$",     # 16 digits, starts with 51-55
		"American Express": r"^3[47][0-9]{13}$", # 15 digits, starts with 34 or 37
		"Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$" # 16 digits, starts with 6011 or 65xx
	}
	# Check each pattern and return the company name if matched
	for company, pattern in patterns.items():
		if re.match(pattern, card_number):
			return company
	return None  # Not a valid card format

# Example usage:
test_card = "4111111111111111"
result = is_valid_credit_card(test_card)
if result:
	print(f"Valid card. Company: {result}")
else:
	print("Invalid card format.")
	



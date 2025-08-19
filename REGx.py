# regex for validating a email adress 
import re


def is_valid_email(email):
	# STEP-BY-STEP BREAKDOWN OF EMAIL VALIDATION
	
	# Step 1: Break down the regex pattern into parts
	start_anchor = r"^"                    # Must start at beginning of string
	username_part = r"[a-zA-Z0-9_.+-]+"   # One or more allowed username characters
	at_symbol = r"@"                       # Literal @ symbol
	domain_part = r"[a-zA-Z0-9-]+"         # One or more domain name characters
	dot_literal = r"\."                    # Literal dot (escaped)
	extension = r"com"                     # Must end with "com"
	end_anchor = r"$"                      # Must end at end of string
	
	# Step 2: Combine all parts into complete pattern
	pattern = start_anchor + username_part + at_symbol + domain_part + dot_literal + extension + end_anchor
	print(f"Complete pattern: {pattern}")
	
	# Step 3: Use re.match to check if email matches pattern
	match_result = re.match(pattern, email)
	print(f"Match result object: {match_result}")
	
	# Step 4: Check if match was found (not None)
	if match_result is not None:
		is_valid = True
	else:
		is_valid = False
	print(f"Is valid email? {is_valid}")
	
	# Step 5: Return the result
	return is_valid

	# Returns True if the email matches the pattern, False otherwise

# Example usage with detailed output:
print("=== Testing Email Validation ===")
test_email = "john.doe+test@gmail.com"
print(f"Testing email: {test_email}")
print()
result = is_valid_email(test_email)
print(f"\nFinal result: {result}")
print()

# Test with invalid email
print("=== Testing Invalid Email ===")
invalid_email = "invalid-email"
print(f"Testing email: {invalid_email}")
print()
result2 = is_valid_email(invalid_email)
print(f"\nFinal result: {result2}")

# Original compact version for comparison:
def original_is_valid_email(email):
	pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com$"
	return re.match(pattern, email) is not None



# import re
# # Import the regular expressions module

# def is_valid_credit_card(card_number):
# 	# Define regex patterns for each card company
# 	patterns = {
# 		"Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",  # 13 or 16 digits, starts with 4
# 		"MasterCard": r"^5[1-5][0-9]{14}$",     # 16 digits, starts with 51-55
# 		"American Express": r"^3[47][0-9]{13}$", # 15 digits, starts with 34 or 37
# 		"Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$" # 16 digits, starts with 6011 or 65xx
# 	}
# 	# Check each pattern and return the company name if matched
# 	for company, pattern in patterns.items():
# 		if re.match(pattern, card_number):
# 			return company
# 	return None  # Not a valid card format

# # Example usage:
# test_card = "4111111111111111"
# result = is_valid_credit_card(test_card)
# if result:
# 	print(f"Valid card. Company: {result}")
# else:
# 	print("Invalid card format.")
	



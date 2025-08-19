# # print("Enter your name:")
# # name = input()
# # print(f"Hello {name}")

import email
import re


is_valid_email = False
while is_valid_email == False:
    x = input("Enter an email:")

    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com$"
    match_result = re.match(pattern, x)
    print(f"Match result object: {match_result}")
    if match_result is None:
        is_valid_email = False
    else:
        is_valid_email = True
    print(f"Is valid email? {is_valid_email}")
#   except Exception as e:
#     print("Wrong input, please try again.")

print("Thank you!")
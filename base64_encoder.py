#! usr/bin/env python3
# importing modules
import base64 

# user input
code = input("Enter string to covert to base64: ")

# coverting into base64
sample_string = code

sample_string_bytes = sample_string.encode("ascii") 

  
# coverting into bytes
base64_bytes = base64.b64encode(sample_string_bytes) 

base64_string = base64_bytes.decode("ascii") 

  
# printing results
print(f"Encoded string: {base64_string}") 

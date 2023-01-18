# FOCP FINAL TASK 4
import sys
if len(sys.argv) < 2: #checking the argv is ture or not
    print("Usage: caesar_cracker.py <encrypted_message_file>") 
    sys.exit(1)
filename = sys.argv[1] #splliting file name 
validate1= " the " #according to zipf law the most repeated word in english is "the"
validate2= " is " #according to zipf law the second most repeated word in english is "is"
try:
    with open(filename, "r") as f:
        encrypted_message = f.read()
        possibility=1
except IOError:
    print("Cannot open '{}'. Sorry about that.".format(filename))
    sys.exit(1)
for shift in range(26):
    decrypted_message = ""
    for ch in encrypted_message:
        if ch.isalpha():
            if ch.isupper():
                decrypted_message += chr((ord(ch) - ord("A") + shift) % 26 + ord("A")) #using the "chr" python function to decrpty the message in ucase
            else:
                decrypted_message += chr((ord(ch) - ord("a") + shift) % 26 + ord("a")) #using the "chr" python function to decrpty the message in lcase
        else:
            decrypted_message += ch
    if validate1 in decrypted_message or validate2 in decrypted_message:
        print("\nPossibility {} Shift {}: {}\n".format(possibility, shift, decrypted_message))
        possibility+=1
    else:
        pass
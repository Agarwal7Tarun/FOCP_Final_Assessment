# FOCP FINAL TASK 4
import sys
if len(sys.argv) < 2:
    print("Usage: caesar_cracker.py <encrypted_message_file>")
    sys.exit(1)
filename = sys.argv[1]
validate1= " the "
validate2= " is "
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
                decrypted_message += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
            else:
                decrypted_message += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        else:
            decrypted_message += ch
    if validate1 in decrypted_message or validate2 in decrypted_message:
        print("\nPossibility {} Shift {}: {}\n".format(possibility, shift, decrypted_message))
        possibility+=1
    else:
        pass
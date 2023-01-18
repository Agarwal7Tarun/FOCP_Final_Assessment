# FOCP FINAL TASK 3
import sys
import random

def main():
  if len(sys.argv) != 2: #checking if the argv is true 
    print("Error: Missing command-line argument.") 
    return

try:
    with open(sys.argv[1], 'r') as input_file:
      with open('student_emails.txt', 'w') as output_file:
        for line in input_file:
          student_id, name = line.strip().split(' ', 1) #splliting the name and id number using index number
          surname, forenames = name.split(',')
          surname = ''.join(c for c in surname if c.isalpha())
          initials = '.'.join(c[0] for c in forenames.split())
          random_digits = ''.join(str(random.randint(0, 9)) for _ in range(4)) #creating email id using for loop for random numbers
          email = f"{initials}.{surname}{random_digits}@poppleton.ac.uk" 
          output_file.write(f"{student_id} {email.lower()}\n") #appending to the file
except IOError:
    print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.") #error message incase the file is not supported

if __name__ == '__main__':
  main()
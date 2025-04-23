import csv

with open("Q3.vcf", "w") as f:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    
    f.write(f"N:{name}\n")
    f.write(f"TEL:{phone}\n")
    f.write(f"EMAIL:{email}\n")
    
    f.write("END:VCARD\n")

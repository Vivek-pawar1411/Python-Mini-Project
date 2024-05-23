
while True:
    mail_id = input("Enter the mail id:- ")  # Example: vivek@14

    if len(mail_id) >= 7:  # Checking length of mail id if less than 7 it gives an error
        
        if mail_id[0].isalpha():   # Check mail_id contains first letter should be alphabet
            
            if "@" in mail_id and mail_id.count("@") == 1:   # Check mail contains maximum one @
                
                if any(char.isdigit() for char in mail_id):  # Check if any digit is present in the mail ID
                    
                    if "gmail.com" not in mail_id:  # Check if "gmail.com" is present  in the end of  mail ID
                        print("Mail ID should contain 'gmail.com'")
                    else:
                        break
                else:
                    print("Mail ID should contain at least one digit")
                
            else:
                print("Mail ID should contain exactly one '@'")
           
        else:
            print("First letter should be alphabet") 
    else:
        print("Length is too short")

print("Mail ID is valid:", mail_id)

from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

number = input("Enter a number : ")
if number.isdigit() and len(number) == 10:
    
    data = supabase.table("users").select("*").eq("id", number).execute()
    print(data)
    if data.data == []:
        username = input("Enter user name : ")
        data = supabase.table("users").insert({"id": number, "username": username}).execute()
        print(f"Welcome {username}! Start shopping now.\n")
    else:
        print(f"Welcome {data.data[0]['username']}! Start shopping now.\n")

else:
    print("Invalid number. Please enter a 10-digit number.\n")
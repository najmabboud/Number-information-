import phonenumbers
from phonenumbers import geocoder, carrier
import tkinter as tk
from tkinter import messagebox

def get_phone_info(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get the country and location
        country = geocoder.country_name_for_number(parsed_number, "ar")
        location = geocoder.description_for_number(parsed_number, "ar")

        # Get the carrier
        phone_carrier = carrier.name_for_number(parsed_number, "ar")

        # Create the message
        message = (
            f"الرقم: {phone_number}\n"
            f"الدولة: {country}\n"
            f"الموقع: {location}\n"
            f"شركة الاتصالات: {phone_carrier}"
        )

        # Show the message in a messagebox
        messagebox.showinfo("معلومات الهاتف", message)
    except phonenumbers.NumberParseException:
        messagebox.showerror("خطأ", "الرقم المدخل غير صالح")

# Function to get input from the user
def get_input():
    phone_number = entry.get()
    get_phone_info(phone_number)

# Create the main window
root = tk.Tk()
root.title("معلومات الهاتف")

# Create and place the widgets
tk.Label(root, text="أدخل رقم الهاتف بصيغة دولية (مثل +1234567890):").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
tk.Button(root, text="احصل على المعلومات", command=get_input).pack(pady=10)

# Run the main loop
root.mainloop()
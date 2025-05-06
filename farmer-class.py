import re

class Farmer:
    def __init__(self, name, email, phone_number, farm_name, farm_location, crops):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.farm_name = farm_name
        self.farm_location = farm_location
        self.crops = crops
        
    def description(self):
        return f"Farmer {self.name} owns {self.farm_name} farm located at {self.farm_location}."
    
    def get_farm_info(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "farm_name": self.farm_name,
            "farm_location": self.farm_location,
            "crops": self.crops
        }

    @staticmethod
    def label_crops(crops):
        labeled_crops = {}
        for crop in crops:
            if crop.lower() in ['carrot', 'spinach', 'broccoli', 'lettuce', 'cabbage']:
                labeled_crops[crop] = 'Vegetable'
            elif crop.lower() in ['apple', 'banana', 'mango', 'orange', 'grape']:
                labeled_crops[crop] = 'Fruit'
            elif crop.lower() in ['wheat', 'rice', 'corn', 'barley', 'oats']:
                labeled_crops[crop] = 'Grain'
            else:
                labeled_crops[crop] = 'Other'
        return labeled_crops

# Function to validate email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Function to get farmer details from user input
def get_farmer_details():
    name = input("Enter farmer's name: ")

    # Validate email
    while True:
        email = input("Enter farmer's email: ")
        if is_valid_email(email):
            break
        else:
            print("Invalid email format. Please enter a valid email.")

    # Validate phone number
    while True:
        phone_number = input("Enter farmer's phone number (digits only): ")
        if phone_number.isdigit():
            break
        else:
            print("Phone number must contain digits only.")

    farm_name = input("Enter farm name: ")
    farm_location = input("Enter farm location: ")

    print("Enter at least 5 crops (type 'done' when finished):")
    crops = []
    while len(crops) < 5:
        crop = input(f"Crop {len(crops) + 1}: ")
        if crop.lower() == 'done' and len(crops) >= 5:
            break
        elif crop.lower() == 'done':
            print("Please enter at least 5 crops.")
        else:
            crops.append(crop)

    labeled_crops = Farmer.label_crops(crops)
    return Farmer(name, email, phone_number, farm_name, farm_location, labeled_crops)

# Main program
if __name__ == "__main__":
    farmer = get_farmer_details()
    print("\nFarmer Details:")
    print(farmer.description())
    print("\nFarm Information:")
    for key, value in farmer.get_farm_info().items():
        print(f"{key.capitalize()}: {value}\n")

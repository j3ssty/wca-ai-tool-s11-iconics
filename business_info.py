# business_info.py

# Core Business Details
BUSINESS_NAME = "Mahanaim Café"
CUISINE_TYPE = "Modern African and Continental Fusion"
PRICE_RANGE = "Affordable to Mid-range"

# Operating Hours
OPENING_HOURS = {
    "Monday": "7:00 AM - 8:00 PM",
    "Tuesday": "7:00 AM - 8:00 PM",
    "Wednesday": "7:00 AM - 8:00 PM",
    "Thursday": "7:00 AM - 8:00 PM",
    "Friday": "7:00 AM - 9:00 PM",
    "Saturday": "8:00 AM - 9:00 PM",
    "Sunday": "8:00 AM - 8:00 PM"  # Matches your example
}

# Contact & Location Info
CONTACT_INFO = {
    "Location": "Thika Road, Near Mahanaim Educational Institute, Nairobi, Kenya",
    "Phone": "+254 700 000000",
    "Email": "info@mahanaimcafe.com",
    "Website": "://mahanaimcafe.com",
    "Social Media": "@MahanaimCafe on Instagram and Facebook"
}

# Full Menu Data
MENU = {
    "Hot Drinks": {
        "House Coffee": "KES 200",
        "Café Latte": "KES 250",
        "Cappuccino": "KES 260",
        "Dawa Tea": "KES 220",
        "Masala Tea": "KES 240",
        "Hot Chocolate": "KES 280"
    },
    "Cold Drinks": {
        "Iced Latte": "KES 280",
        "Passion Juice": "KES 200",
        "Mango Smoothie": "KES 350",
        "Classic Milkshake (Vanilla/Chocolate)": "KES 380",
        "Still Water (500ml)": "KES 100"
    },
    "Breakfast & Pastries": {
        "Andazi (Pair)": "KES 80",
        "Samosa (Beef/Chicken, Pair)": "KES 150",
        "Spanish Omelette with Toast": "KES 250",
        "Pancakes with Syrup": "KES 300",
        "Full Mahanaim Breakfast": "KES 550"
    },
    "Main Meals": {
        "Beef Burger with Fries": "KES 600",
        "Grilled Chicken Breast with Rice": "KES 650",
        "Fish Fillet with Ugali and Skuma": "KES 700",
        "Vegetable Stir-fry Noodles": "KES 450",
        "Loaded Fries / Masala Chips": "KES 300"
    }
}

# Frequently Asked Questions (FAQs) & Policies
FAQS = {
    "Wi-Fi": "Yes, we offer free high-speed Wi-Fi to all dining customers. Just ask your server for the password.",
    "Parking": "Ample and secure free parking is available for our customers inside the compound.",
    "Delivery": "Yes, we deliver via Bolt Food and Uber Eats within a 5km radius, or you can call us directly to order.",
    "Reservations": "Walk-ins are highly welcome, but you can book a table for groups of more than 6 people by calling us.",
    "Methods of Payment": "We accept Cash, M-Pesa (Lipa na M-Pesa), and major Credit/Debit Cards.",
    "Events & Catering": "We host small events like birthday parties and business meetings. Contact management via phone or email for catering packages."
}

def get_business_summary() -> str:
    """
    Formats the business data into a single clean string.
    This string will be passed to your system prompt in prompts.py.
    """
    summary = f"Business Name: {BUSINESS_NAME}\n"
    summary += f"Type: {CUISINE_TYPE}\n\n"
    
    summary += "--- OPERATING HOURS ---\n"
    for day, hours in OPENING_HOURS.items():
        summary += f"- {day}: {hours}\n"
        
    summary += "\n--- CONTACT & LOCATION ---\n"
    for key, value in CONTACT_INFO.items():
        summary += f"- {key}: {value}\n"
        
    summary += "\n--- MENU ---\n"
    for category, items in MENU.items():
        summary += f"\n[{category}]\n"
        for item, price in items.items():
            summary += f"  * {item}: {price}\n"
            
    summary += "\n--- ADDITIONAL INFORMATION & POLICIES ---\n"
    for question, answer in FAQS.items():
        summary += f"- {question}: {answer}\n"
        
    return summary

# Quick test to make sure formatting works properly
if __name__ == "__main__":
    print(get_business_summary())

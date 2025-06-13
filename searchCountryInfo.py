from countryinfo import CountryInfo

# Input from user
country_name = input("Enter your country name: ")

try:
    # Create a CountryInfo object for the given country
    country = CountryInfo(country_name)
    
     # Fetch all available country information in a dictionary
    info = country.info()
    
    # Display the country details
    print(f"\n🌍 You entered: {country_name.title()}\n📍 Here are the details.")
    print("🏛️ Capital: ",info.get("capital", "Not available"))
    print("💱 Currency: ",info.get("currencies", "Not available"))
    print("🗣️ Language(s): ",info.get("languages", "Not available"))
    print("🗺️ Border(s): ", info.get("borders", "Not available"))
    print("🕒 Time zone: ", info.get("timezones", "Not available"))
    print("👥 Population: ", info.get("population", "Not available"))
    
except KeyError:
    # Handle cases where certain details are missing in the API response
    print("❌ Error: Some details for not found this country.")
    
except Exception as e:
    # Handle other unexpected errors.
    print("❌ Invalid input or data not available. Please recheck the country name.")
    print("Error",str(e))

from bs4 import BeautifulSoup as BS
import requests as req
import pyfiglet
import sys
print(sys.executable)

def mainMenu():
    result = pyfiglet.figlet_format("Al Jazeera News", font="slant")
    print(result)
    print("1. Middle East")
    print("2. US & Canada")
    print("3. Europe")
    print("4. Exit")
    
    choice = input("Choose a number: ")
    
    if choice in ['1','2','3']:
        scraper(choice)
    elif choice == '4':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        mainMenu()
        
def pageToScrape(choice):
    if choice == '1':
        return req.get("https://www.aljazeera.com/middle-east/")
    elif choice == '2':
        return req.get("https://www.aljazeera.com/us-canada/")
    elif choice == '3':
        return req.get("https://www.aljazeera.com/europe/")
    
def scraper(choice):
    response = pageToScrape(choice)
    if response:
        soup = BS(response.text, "html.parser")
        headLines = soup.findAll("a", attrs={"class":"u-clickable-card__link"})
        if headLines:
            print("\nHeadlines:")
            print("-" * 40)
            for idx, headLine in enumerate(headLines, start=1):
                print(f"{idx}. {headLine.text.strip()}")
                print("-" * 40)
        else:
            print("No headlines found.")
    else:
        print("Failed to retrieve the page.")

if __name__ == "__main__":
    mainMenu()

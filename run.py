from math import e
from insite.insite_utility.bodynavigation import BodyNavigation
from insite.main_insite import Insite
from insite.login import LoginFlow
from insite.insite_utility.interaction import Interaction
from insite.insite_utility.contact import ContactUs
import traceback


def run_registration(bot, plan_choice):
    try:
        if plan_choice in ['1', '2', '3']:
            print("\n=== Starting Registration Process ===")
            print("Navigating to the website...")
            bot.landing_first_page()
            print("✓ Successfully loaded the Home page")

            print("\nAccepting cookies...")
            bot.accept_cokkies()
            print("✓ Cookies accepted")

            print("\nClicking 'Get Insite Free' (Button)...")
            bot.get_insite_free()
            print("✓ Successfully clicked 'Get Insite Free'")

            if plan_choice == '1':
                print("\nClicking beta pricing plan (Button)...")
                bot.click_beta_pricing_plan()
                print("✓ Beta pricing button Passed")
            elif plan_choice == '2':
                print("\nClicking Personal pricing plan (Button)...")
                bot.click_personal_pricing_plan()
                print("✓ Personal pricing button worked")

            elif plan_choice == '3':
                print("\nClicking Team pricing plan (Button)...")
                bot.click_team_pricing_plan()
                print("✓ Team pricing button worked")
        else:
            print("Invalid choice Please choose between 1 to 3.")
            return False

        print("\nStarting email verification...")
        bot.email_verification()
        print("✓ Email verification completed")

        print("\nStarting onboarding questions...")
        bot.onboarding_questioner()
        print("✓ Successfully completed onboarding")

        print("\nStarting extension download...")
        bot.download_extension()
        print("✓ Extension download process started")
        
        input("\n✓ Registration completed successfully! Press Enter to exit...")
        return True
    except Exception as e:
        print(f"\n✗ Error during registration: {str(e)}")
        traceback.print_exc()
        return False

def run_login(bot):
    try:
        print("\n=== Starting Login Process ===")
        # Step 1: Navigate to the main page
        print("1. Navigating to the website...")
        bot.landing_first_page()
        print("   ✓ Page loaded successfully")
        # Step 2: Accept cookies
        print("\n2. Accepting cookies...")
        bot.accept_cokkies()
        print("   ✓ Cookies accepted")
        # Initialize LoginFlow
        login_flow = LoginFlow(bot.driver)
        # Step 3: Start login process
        print("\n3. Starting login process...")
        login_flow.login_processing()
        print("   ✓ Login button clicked")
        bot.download_extension()
        # Step 4: Handle sign text (new tab)    
        print("\n4. Processing sign in...")
        login_flow.sign_text("1tpvzbiz03@its34bpl.mailosaur.net", "YourPassword123!")
        print("   ✓ Sign in page loaded")  
        print("\n✓ Login process completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n✗ Error during login process: {str(e)}")
        traceback.print_exc()
        return False

def run_dashboard(bot):
    try:
        #1 Navigate to the main page
        print("1. Navigating to the website...")
        bot.landing_first_page()
        print("   ✓ Page loaded successfully")
        # Step 2: Accept cookies
        print("2. Accepting cookies...")
        bot.accept_cokkies()
        print("   ✓ Cookies accepted")
        #initliaze interaction file
        interaction_flow = Interaction(bot.driver)
        print("3. Starting the Dashboard Navigation")
        interaction_flow.interact_with_buttons()
        return True
    except Exception as e:
        print(f"✗ Error during Interaction process: {str(e)}")
        traceback.print_exc()
        return False

def run_body(bot):
    try:
        print("1. Navigating to the Homepage...")
        bot.landing_first_page()
        print("   ✓ Page loaded successfully")
        # Accept cokkies section
        print("2. Accepting Cookies...")
        bot.accept_cokkies()
        print("   ✓ Cookies Accepted")
        #Initialization of body navigation
        body_caller = BodyNavigation(bot.driver)
        #Now starting the Body Navigation processing...
        print("3. Starting the Body Navigation...")
        body_caller.interact_with_body()
        return True
    except Exception as e:
        print(f"✗ Error during the body navigation process: {str(e)}")
        traceback.print_exc()
        return False

def run_contact(bot):
    try:
        print("1. Navigating to the Homepage...")
        bot.landing_first_page()

        #Accepting coookies
        print("2. Accepting Cookies...")
        bot.accept_cokkies()

        #Initialization 
        contact_caller = ContactUs(bot.driver)

        #Now startting the process of contact us filling
        contact_caller.filling_contact()
        print("Contact form testing successfully.")
        
        return True

    except Exception as e:
        print(f"✗ Error during the contact us testing process: {str(e)}")
        traceback.print_exc()
        return False

        



def main():
    #only to delcear the variable 
    navi = "Navigation"

    print("\n=== Insite Bot ===")
    print("1. Registration")
    print("2. Login")
    print("3. Dashboard Navigation")
    print("4. Body Navigation")
    print("5. Contact Us (Form)")
    
    # Move user input before browser opens
    while True:
        choice = input(f"\nChoose mode (1 = registration, 2 = login, 3 = Dashboard {navi}, 4 = Body {navi}, 5 = Contact Us (form)) : ").strip()
        if choice in ["1", "2" , "3", "4", "5"]:
            break
        print("Invalid choice. Please enter 1 , 2 , 3 , 4 or 5.")

    plan_choice = None
    if choice == "1":
        while True:
            plan_choice = input("\nChoose pricing plan (1 = Free pass Plan, 2 = Personal free plan, 3 = Team plan): ").strip()
            if plan_choice in ['1', '2', '3']:
                break
            print("Invalid choice. Please choose between 1 to 3.")
    
    # Set teardown to False to prevent automatic browser closing
    with Insite(teardown=False) as bot:
        if choice == "1":
            run_registration(bot, plan_choice)

        elif choice == '2':
            run_login(bot)
        elif choice == '3':
            run_dashboard(bot)
        elif choice == '4':
            run_body(bot)
        elif choice == '5':
            run_contact(bot)
        else:
            pass

        # Wait for user to press Enter before closing
    input("Press Enter to close the browser and exit...")
    # Manually close the browser when user is done
    bot.driver.quit()

if __name__ == "__main__":
    main()


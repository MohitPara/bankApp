import json
import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engines.options_engine import OptionsEngine


def main():
    # Get the JSON file path - use the one from the original project
    json_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'AccDtl.json')
    
    print("Creating Account - 1")
    print("Updating Account Detail - 2")
    print("Delete Account - 3")
    print("Depositting mony - 4")
    print("Withdrawing mony - 5")
    print("Account Detail - 6")
    print("")

    options_engine = OptionsEngine(json_file_path)
    
    while True:
        option = input("Choose your option: ")
        
        if option:
            if option == "1":
                options_engine.create_acc()
            elif option == "2":
                options_engine.update_acc()
            elif option == "3":
                options_engine.delete_acc()
            elif option == "4":
                options_engine.deposit_mony()
            elif option == "5":
                options_engine.withwrew_mony()
            elif option == "6":
                options_engine.acc_detail()
            else:
                print("option not present")
            
            print("Do you want to continue yes/no")
            print("")
            option1 = input()
            
            if not option1 or option1.strip().lower() != "yes":
                # Save data before exiting
                options_engine._save_data()
                break
        else:
            print("Choose your option correctly")


if __name__ == "__main__":
    main()

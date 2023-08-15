def dog():
    print(" ^   ^")
    print("૮ ・ﻌ・ა")
    print("૮       ა")
    print("  ฅ   ฅ")

def askdog():
    print("Wanna see a lovely creature? (yes/no)")
    user_input = input()
    if user_input.lower() == "yes":
        dog()
    elif user_input.lower() == "no":
        print("Are you sure? (yes/no)")
        confirm_input = input()
        if confirm_input.lower() == "yes":
            dog()
        elif confirm_input.lower() == "no":
            print("I'm gonna show you anyway!")
            dog()
        else:
            print("Please enter 'yes' or 'no'.")
    else:
        print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    askdog()
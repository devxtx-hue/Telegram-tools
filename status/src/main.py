
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

API_ID = input("Enter API_ID" )  
API_HASH = input("Enter API_HASH" )  
PHONE_NUMBER = input("Enter Phone number ")  


STATUSES = {
    "1": {"name": "Active", "emoji": "🏃", "about": "Alive"},
    "2": {"name": "Busy", "emoji": "🚫", "about": "Busy"},
    "3": {"name": "Sleep", "emoji": "💤", "about": "sleep"}
}

async def change_status(status_key):
    if status_key not in STATUSES:
        return False, "N/A status"
    
    status = STATUSES[status_key]
    
    try:
        async with TelegramClient('session', API_ID, API_HASH) as client:
            await client.start(PHONE_NUMBER)
            
            await client(UpdateProfileRequest(about=status["about"]))
            
            return True, f"status changed to : {status['emoji']} {status['name']}"
            
    except Exception as e:
        return False, f"err: {str(e)}"

async def show_current_status():
    try:
        async with TelegramClient('session', API_ID, API_HASH) as client:
            await client.start(PHONE_NUMBER)
            me = await client.get_me()
            
            if me.about:
                return f" current status: {me.about}"
            else:
                return ""
                
    except Exception as e:
        return f"err: {str(e)}"

def print_menu():
    print("\n" + "="*40)
    print("manager status telegram")
    print("="*40)
    
    for key, status in STATUSES.items():
        print(f"{key}) {status['emoji']} {status['name']}")
        print(f"   {status['about']}")
        print()
    
    print("c) show current status")
    print("q) exit")
    print("="*40)

async def main():
    print("Starting Manager")
    
    while True:
        print_menu()
        choice = input("\nChoice").strip().lower()
        
        if choice == 'q':
            print("exit..")
            break
            
        elif choice == 'c':
            current = await show_current_status()
            print(f"\n{current}")
            input("\nPress enter to countine")
            
        elif choice in STATUSES:
            print(f"\nchange status {STATUSES[choice]['emoji']}...")
            success, message = await change_status(choice)
            
            if success:
                print(f"{message}")
            else:
                print(f"{message}")
                
            input("\nPress enter to continue")
            
        else:
            print("N/A choice try again")
            input("\nPress enter to continue")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit..")
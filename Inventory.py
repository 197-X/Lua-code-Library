class InventorySystem:
    def __init__(self):
        self.module = ["Grab", "Punch", "Hammer"]
        self.hotbar = None
    
    def display_module(self):
        """Display all items in the module"""
        print("\n=== MODULE ===")
        if not self.module:
            print("No items available")
        else:
            for idx, item in enumerate(self.module, 1):
                print(f"{idx}. {item}")
    
    def display_hotbar(self):
        """Display the current hotbar slot"""
        print("\n=== HOTBAR ===")
        if self.hotbar:
            print(f"[{self.hotbar}]")
        else:
            print("[Empty]")
    
    def add_to_hotbar(self):
        """Add an item from module to hotbar"""
        if not self.module:
            print("\nNo items available in module!")
            return
        
        self.display_module()
        try:
            choice = input("\nEnter the number of the item to add to hotbar: ")
            idx = int(choice) - 1
            
            if 0 <= idx < len(self.module):
                self.hotbar = self.module[idx]
                print(f"\n'{self.hotbar}' added to hotbar!")
            else:
                print("\nInvalid selection!")
        except ValueError:
            print("\nPlease enter a valid number!")
    
    def remove_from_hotbar(self):
        """Remove item from hotbar"""
        if self.hotbar:
            print(f"\n'{self.hotbar}' removed from hotbar!")
            self.hotbar = None
        else:
            print("\nHotbar is already empty!")
    
    def add_item_to_module(self):
        """Add a new item to the module"""
        item_name = input("\nEnter the name of the new item: ").strip()
        if item_name:
            self.module.append(item_name)
            print(f"\n'{item_name}' added to module!")
        else:
            print("\nItem name cannot be empty!")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*30)
        print("INVENTORY SYSTEM")
        print("="*30)
        self.display_hotbar()
        print("\nOptions:")
        print("1. View Module")
        print("2. Add item to Hotbar")
        print("3. Remove item from Hotbar")
        print("4. Add new item to Module")
        print("5. Exit")
    
    def run(self):
        """Main loop for the inventory system"""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == "1":
                self.display_module()
            elif choice == "2":
                self.add_to_hotbar()
            elif choice == "3":
                self.remove_from_hotbar()
            elif choice == "4":
                self.add_item_to_module()
            elif choice == "5":
                print("\nExiting inventory system. Goodbye!")
                break
            else:
                print("\nInvalid choice! Please enter 1-5.")


# Run the inventory system
if __name__ == "__main__":
    inventory = InventorySystem()
    inventory.run()

class Player:
    def __init__(self, name, location):
        self.name = name
        self.items = []
        self.location = location

    def move(self, new_location):
        self.location = new_location
        print("You moved to:", self.location.name)

    def collect_item(self):
        if self.location.item is not None:
            item = self.location.item 
            self.items.append(item)
            self.location.item = None
            print("You collected:", item.name)
        else:
            print("There is no item here. :( ")

    def show_inventory(self):
        print("\nYour inventory:")


        if len(self.items) == 0:
            print("Your Inventory is empty. :( ")
        else: 
            for item in self.items:
                print(item.name, "-", item.weight, "kg")
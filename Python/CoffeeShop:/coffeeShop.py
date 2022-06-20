class CoffeeShop:
	def __init__(self, name, menu, orders):
		self.name = name
		self.menu = menu
		self.orders = orders
		self.total_due = 0
		self.item_prices = {d["item"] : d["price"] for d in self.menu}
		
	def add_order(self, item):
		if item in [d["item"] for d in self.menu]:
			self.total_due += self.item_prices[item]
			self.orders.append(item)
			return "Order added!"
		
		return "This item is currently unavailable!"
			
			
	def fulfill_order(self):
		if self.orders:
			self.total_due -= self.item_prices[self.orders[0]]
			is_it_ready = "The {} is ready!".format(self.orders[0])
			self.orders = self.orders[1:]
			return is_it_ready
		return "All orders have been fulfilled!"
	
	def list_orders(self): return self.orders
	
	def due_amount(self):
		return round(sum(self.item_prices[i] for i in self.orders),2)
			
	def cheapest_item(self):
		return min(self.menu, key=lambda d: d["price"])["item"]
		
	def drinks_only(self):
		return [d["item"] for d in self.menu if d["type"] == "drink"]
		
	def food_only(self):
		return [d["item"] for d in self.menu if d["type"] == "food"]

		
		
		
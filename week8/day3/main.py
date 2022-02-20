
class Door():
	def __init__(self, is_opened):
		self.is_opened = is_opened
	def open_door(self):
		self.is_opened = True

	def close_door(self):
		self.is_opened = False

class BlockedDoor(Door):
	pass


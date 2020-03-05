
# https://medium.com/better-programming/decorators-in-python-72a1d578eac4

def sandwitch(x):
	def inside(*args, **kwargs):
		return "Sandwich " + x(*args, **kwargs)
	return inside

@sandwitch
def ham(meat=None):
	if meat:
		return meat + " ham"
	return "Ham"


print ham(meat="chicken")


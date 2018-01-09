"""Print out all the melons in our inventory."""


from melons import melon_info


def print_melon():
    """Print each melon."""
    for melon in melon_info.keys():
    	print melon.upper()
    	characteristics = {"seedless", "price", "flesh_color", "weight", "rind_color"}
    	for characteristic in characteristics:
    		print characteristic + ":" + str(melon_info[melon].get(characteristic))
    	print '==================================='

print_melon()
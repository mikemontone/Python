magic_list = ['harry houdini','harry potter','merlin']
magic_list_great = []

def show_magicians(names):
    """Displays the name of magicians in the magic_list. """
    for name in names:
        msg = "Introducing, " + name.title() + "!"
        print(msg)

def make_great(names):
    """ Adds "the Great" to the list of names in magic_list,modifies the list. """
    while magic_list:
        current_name = magic_list.pop() + " the Great"
        magic_list_great.append(current_name)
        msg = "Introducing, " + current_name.title() 
        print(msg)

show_magicians(magic_list)
make_great(magic_list)
print(magic_list)

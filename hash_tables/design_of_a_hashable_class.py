

# 3. Design of a hashable class

class ContactList:
    def __init__(self, names):
        # name is a list of strings.
        self.names = names

    def __hash__(self):
        # conceptually we want to hash the set of names. Since the set type is
        # mutable, it cannot be hashed. Therefore we use frozenset.
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)



def merge_contact_lists(contacts):
    # contacts is a list of contactlist.
    return list(set(contacts))
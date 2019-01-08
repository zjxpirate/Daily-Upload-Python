




from Linked_Lists_sentinel_DLL import Sentinel_DLL


def test_sentinel_DLL():
    l = Sentinel_DLL()
    l.append("Maine")
    l.append("Idaho")
    l.append("Utah")


    node = l.find("Idaho")
    if node != None:
        print(node.get_data())
        l.insert_after(node, "Ohio")
    print(l)


    if node != None:
        l.delete(node)
    print(l)


    while l.first_node() != None:
        l.delete(l.first_node())
    print(l)


test_sentinel_DLL()




"""
Allow a simple h5py walk to more easily put the database into a dictionary
"""

import h5py
import re


def write_dict(d, h5root):
    """
    Given a nested dictionary, write an h5 file with a tree-structure matching
     the nesting (using generators)
    """
    for key, value in d.items():
        # print(key)
        if isinstance(value, dict):
            if key not in h5root:
                h5sub = h5root.create_group(key)
            else:
                h5sub = h5root.get(key)
            yield from write_dict(value, h5sub)
        else:
            yield key, value, h5root


def getdbvals(node, exclude=[], verbose=False):
    """Traverse an h5py node and stuff results into nested dictionary"""

    d = {}
    parent = str(node.name)

    def get_rel_name(fullname, parent):
        return re.sub(parent + "/", "", fullname)

    def get_items(name, item, d=d, parent=parent):
        # visititems gives full path instead of sub-path like we want
        itemstr = get_rel_name(str(item.name), parent)
        itemlst = itemstr.split("/")

        # if intersection is non-zero
        if list(set(exclude) & set(itemlst)):
            return
        p = d
        if isinstance(item, h5py.Dataset):
            for x in itemlst[:-1]:
                p = p.setdefault(x, {})
            p = p.setdefault(itemlst[-1], item[()])
            if verbose:
                print("      ", itemstr)
        elif isinstance(item, h5py.Group):
            if verbose:
                print("      ", itemstr)
        else:
            print("Problem with " + itemstr, type(item))

    node.visititems(get_items)
    return d

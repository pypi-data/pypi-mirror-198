# Copyright (C) 2021 Phoebe Pearce
#
# This file is part of RayFlare and is released under the GNU General Public License (GPL), version 3.
# Please see the LICENSE.txt file included as part of this package.
#
# Contact: p.pearce@unsw.edu.au

from collections import OrderedDict


class State(OrderedDict):
    """This class defines a convent way of expanding the attributes of an object, usually fixed during the definition of
    the class. In this case, the class is just a dictionary - a special type of it - and attributes are expanded by
    adding new keys to it.
    """

    def __getattr__(self, name):
        # print ("***", name)
        if name in ["_OrderedDict__root", "_OrderedDict__map"]:
            return OrderedDict.__getattribute__(self, name)

        if name in self:
            return self[name]
        else:
            raise AttributeError(
                "The state object does not have an entry for the key '%s'." % (name,)
            )

    def __setattr__(self, name, value):
        if name in [
            "_OrderedDict__root",
            "_OrderedDict__map",
            "_OrderedDict__hardroot",
        ]:
            return OrderedDict.__setattr__(self, name, value)

        self[name] = value

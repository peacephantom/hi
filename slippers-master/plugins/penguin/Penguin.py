from world.dataHandler.pluginManager.Plugin import Plugin

class Penguin(Plugin):
    """
    A plugin that enables essential player features.
    """

    def __init__(self, users, rooms, packet):
        super(Penguin, self).__init__(users, rooms, packet)

    def heartbeat(self, data, user):
        user.send(["h", "-1"])

    def buddy_list(self, data, user):
        user.send(["bl", "-1"])

    def ignore_list(self, data, user):
        user.send(["nl", "-1"])

    def item_list(self, data, user):
        user.send(["il", "-1"])

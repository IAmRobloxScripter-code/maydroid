import logging
import tools.helpers.props
import tools.helpers.ipc
import dbus

def get(args):
    try:
        session_bus_id = getattr(args, "instance_id", "default")
        tools.helpers.ipc.DBusSessionService(session_bus_id)

        cm = tools.helpers.ipc.DBusContainerService(session_bus_id)
        session = cm.GetSession()
        if session["state"] == "FROZEN":
            cm.Unfreeze()

        ret = tools.helpers.props.get(args, args.key)
        if ret:
            print(ret)

        if session["state"] == "FROZEN":
            cm.Freeze()
    except (dbus.DBusException, KeyError):
        logging.error("WayDroid session is stopped")

def set(args):
    try:
        session_bus_id = getattr(args, "instance_id", "default")
        tools.helpers.ipc.DBusSessionService(session_bus_id)

        cm = tools.helpers.ipc.DBusContainerService(session_bus_id)
        session = cm.GetSession()
        if session["state"] == "FROZEN":
            cm.Unfreeze()

        tools.helpers.props.set(args, args.key, args.value)

        if session["state"] == "FROZEN":
            cm.Freeze()
    except (dbus.DBusException, KeyError):
        logging.error("WayDroid session is stopped")

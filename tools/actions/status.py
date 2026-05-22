# Copyright 2021 Erfan Abdi
# SPDX-License-Identifier: GPL-3.0-or-later
import tools.config
import tools.helpers.ipc
import tools.helpers.net
import dbus

def print_status(args):
    session_bus_id = getattr(args, "instance_id", "default")
    cfg = tools.config.load(args)
    def print_stopped():
        print(f"Session_{session_bus_id}: STOPPED")
        print("Vendor type: " + cfg["waydroid"]["vendor_type"])

    try:
        session = tools.helpers.ipc.DBusContainerService(session_bus_id).GetSession()
        if session:
            print(f"Session_{session_bus_id}: RUNNING")
            print(f"Container_{session_bus_id}: " + session["state"])
            print("Vendor type: " + cfg["waydroid"]["vendor_type"])
            print("IP address: " + (tools.helpers.net.get_device_ip_address() or "UNKNOWN"))
            print("Session user: {}({})".format(session["user_name"], session["user_id"]))
            print("Wayland display t" + session["wayland_display"])
        else:
            print_stopped()
    except dbus.DBusException:
        print_stopped()

# Copyright 2022 Alessandro Astone
# SPDX-License-Identifier: GPL-3.0-or-later

# Currently implemented as FIFO
import os
import dbus

def DBusContainerService(instance_id="default",object_path="/ContainerManager", intf="id.waydro.ContainerManager"):
    return dbus.Interface(dbus.SystemBus().get_object(f"id.waydro.Container.{instance_id}", object_path), intf)

def DBusSessionService(instance_id="default", object_path="/SessionManager", intf="id.waydro.SessionManager"):
    return dbus.Interface(dbus.SessionBus().get_object(f"id.waydro.Session.{instance_id}", object_path), intf)

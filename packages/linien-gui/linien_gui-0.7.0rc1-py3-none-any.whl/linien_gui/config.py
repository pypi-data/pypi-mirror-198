# Copyright 2018-2022 Benjamin Wiegand <benjamin.wiegand@physik.hu-berlin.de>
#
# This file is part of Linien and based on redpid.
#
# Linien is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Linien is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Linien.  If not, see <http://www.gnu.org/licenses/>.

import os
import pickle
from enum import Enum

import appdirs
import rpyc

# don't plot more often than once per `DEFAULT_PLOT_RATE_LIMIT` seconds
DEFAULT_PLOT_RATE_LIMIT = 0.1


class Color(Enum):
    SPECTRUM1 = 0
    SPECTRUM2 = 1
    SPECTRUM_COMBINED = 2
    CONTROL_SIGNAL = 0
    CONTROL_SIGNAL_HISTORY = 1
    SLOW_HISTORY = 3
    MONITOR_SIGNAL_HISTORY = 4


def get_data_folder():
    folder_name = appdirs.user_data_dir("linien")

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return folder_name


def get_devices_filename():
    return os.path.join(get_data_folder(), "devices")


def save_device_data(devices):
    with open(get_devices_filename(), "wb") as f:
        pickle.dump(devices, f)


def load_device_data():
    try:
        with open(get_devices_filename(), "rb") as f:
            devices = pickle.load(f)
    except (FileNotFoundError, pickle.UnpicklingError, EOFError):
        devices = []

    return devices


def save_parameter(device_key, param, value, delete=False):
    devices = load_device_data()
    device = [d for d in devices if d["key"] == device_key][0]
    device.setdefault("params", {})

    if not delete:
        # FIXME: This is the only part where rpyc is used in linien-gui. Remove it if
        # possible.
        # rpyc obtain is for ensuring that we don't try to save a netref here
        try:
            device["params"][param] = rpyc.classic.obtain(value)
        except Exception:
            print("unable to obtain and save parameter", param)
    else:
        try:
            del device["params"][param]
        except KeyError:
            pass

    save_device_data(devices)


def get_saved_parameters(device_key):
    devices = load_device_data()
    device = [d for d in devices if d["key"] == device_key][0]
    device.setdefault("params", {})
    return device["params"]

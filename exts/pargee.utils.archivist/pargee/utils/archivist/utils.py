import os
from typing import Set
import omni.usd


def get_current_stage_path():
    try:
        current_path = os.path.split(omni.usd.get_context().get_stage_url())[0]
        return current_path
    except Exception:
        return ""


def get_current_file_name():
    if not omni.usd.get_context().is_new_stage():
        try:
            current_file_name = os.path.split(omni.usd.get_context().get_stage_url())[1]
            current_file_name = os.path.splitext(current_file_name)[0]
            return current_file_name
        except Exception:
            return ""
    return ""


def get_current_stage_dir():
    try:
        current_dir = os.path.basename(os.path.dirname(omni.usd.get_context().get_stage_url()))
        return current_dir
    except Exception:
        return ""


def zero_pad(value):
    if value < 10:
        return "0" + str(value)
    else:
        return str(value)

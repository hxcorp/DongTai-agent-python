import json

import dongtai_agent_python.global_var as dt_global_var


def str_join(o, value):
    if "builtins.str.join" in dt_global_var.dt_get_value("has_patched"):
        return o.join(value, __bypass_dt_agent__=True)
    return o.join(value)


def list_append(o, value):
    if "builtins.list.append" in dt_global_var.dt_get_value("has_patched"):
        return o.append(value, __bypass_dt_agent__=True)
    return o.append(value)


def list_insert(o, idx, value):
    if "builtins.list.append" in dt_global_var.dt_get_value("has_patched"):
        return o.insert(idx, value, __bypass_dt_agent__=True)
    return o.insert(idx, value)


def json_dumps(value):
    if "json.dumps" in dt_global_var.dt_get_value("has_patched"):
        return json.dumps(value, __bypass_dt_agent__=True)
    return json.dumps(value)


def json_loads(value):
    if "json.loads" in dt_global_var.dt_get_value("has_patched"):
        return json.loads(value, __bypass_dt_agent__=True)
    return json.loads(value)


def request_session_get(session, *args, **kwargs):
    if "requests.sessions.Session.request" in dt_global_var.dt_get_value("has_patched"):
        return session.get(*args, **kwargs, __bypass_dt_agent__=True)
    return session.get(*args, **kwargs)


def request_session_post(session, *args, **kwargs):
    if "requests.sessions.Session.request" in dt_global_var.dt_get_value("has_patched"):
        return session.post(*args, **kwargs, __bypass_dt_agent__=True)
    return session.post(*args, **kwargs)


def bytes_decode(value, *args, **kwargs):
    if "builtins.bytes.decode" in dt_global_var.dt_get_value("has_patched"):
        return value.decode(*args, **kwargs, __bypass_dt_agent__=True)
    return value.decode(*args, **kwargs)

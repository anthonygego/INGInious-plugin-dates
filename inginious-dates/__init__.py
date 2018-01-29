import re
from inginious.frontend.accessible_time import AccessibleTime


def task_accessibility(course, task, default):
    dates = course.get_descriptor().get("dates", None)
    if not dates:
        return default

    for pattern in dates.keys():
        if re.match(pattern, task.get_id()):
            return AccessibleTime(dates[pattern])

    return default


def init(plugin_manager, course_factory, client, config):
    plugin_manager.add_hook('task_accessibility', task_accessibility)

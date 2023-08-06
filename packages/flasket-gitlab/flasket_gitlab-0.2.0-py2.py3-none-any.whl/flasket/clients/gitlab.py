from enum import Enum, unique

from flask import request as current_request
from flasket.exceptions import BadRequest, NoContent
from flasket.utils import StringMixin

from flasket import endpoint


@unique
class HTTPHeaders(StringMixin, Enum):
    X_GITLAB_EVENT = "X-Gitlab-Event"
    X_GITLAB_TOKEN = "X-Gitlab-Token"


@unique
class HookEvents(StringMixin, Enum):
    JOB_HOOK = "Job Hook"
    MERGE_REQUEST_HOOK = "Merge Request Hook"
    PIPELINE_HOOK = "Pipeline Hook"
    PUSH_HOOK = "Push Hook"
    SYSTEM_HOOK = "System Hook"
    TAG_PUSH_HOOK = "Tag Push Hook"


def webhook_validate_event(headers, events_allowed=None):
    """
    Validate the headers with X-Gitlab-Event against the allowed values with
    special provisions for the System Event hook that is recieved by all instance wide
    endpoints.

    If events_allowed is None: validation will take place against []
    If events_allowed is True: validation will always be successfull.
    If events_allowed is a list of HookEvents: validation will take place.

    :param headers: request headers
    :param events_allowed: None, True or list of HookEvents
    :raises: :class:`BadRequest`: Missing or invalid header
    :raises: :class:`NoContent`: System event accepted but ignored
    """
    if events_allowed is None:
        events_allowed = []
    if events_allowed is True:
        return

    current_event = headers.get(HTTPHeaders.X_GITLAB_EVENT.value)
    if current_event is None:
        raise BadRequest("Missing required header '%s'" % HTTPHeaders.X_GITLAB_EVENT)

    hook_event = None
    try:
        hook_event = HookEvents(current_event)
    except ValueError:
        raise BadRequest("Invalid value for header '%s'" % HTTPHeaders.X_GITLAB_EVENT)

    if hook_event == HookEvents.SYSTEM_HOOK:
        if HookEvents.SYSTEM_HOOK not in events_allowed:
            raise NoContent

    if hook_event not in events_allowed:
        raise BadRequest("'%s' event is not handled by this endpoint" % current_event)


def webhook(events_allowed):
    """
    Validate the X-Gitlab-Event against the value from decoratored function.
    """

    # TODO: use functools.wraps
    def decorator(fn):
        @endpoint
        def wrapper(app, *args, **kwargs):
            headers = current_request.headers
            webhook_validate_event(headers, events_allowed)
            return fn(app=app, *args, **kwargs)

        return wrapper

    return decorator

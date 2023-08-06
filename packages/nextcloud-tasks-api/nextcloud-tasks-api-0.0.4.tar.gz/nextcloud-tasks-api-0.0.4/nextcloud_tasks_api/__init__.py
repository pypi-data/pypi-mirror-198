from .request import BasicAuthenticator, RequestsRequester
from .api import NextcloudTasksApi, ApiError, TaskList, TaskFile


__all__ = [
    'BasicAuthenticator',
    'RequestsRequester',
    'NextcloudTasksApi',
    'ApiError',
    'TaskList',
    'TaskFile',
    'get_nextcloud_tasks_api',
]


def get_nextcloud_tasks_api(base_url: str,
                            username: str,
                            password: str,
                            verify_ssl: bool = True,
                            stream: bool = True) -> NextcloudTasksApi:
    """Convenience function for API instance on the given endpoint."""
    return NextcloudTasksApi(RequestsRequester(
        base_url=base_url,
        authenticator=BasicAuthenticator(username=username, password=password),
        verify=verify_ssl,
        stream=stream
    ))

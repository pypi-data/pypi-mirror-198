from ligo.rrt_chat import channel_creation, mattermost_api
import os
import stat
import pytest
from unittest.mock import patch


@pytest.fixture
def netrc_mattermost(tmpdir):
    path = str(tmpdir / 'netrc')
    with open(path, 'w') as f:
        os.fchmod(f.fileno(), stat.S_IRWXU)
        print('machine', 'mattermost-bot', file=f)
        print('login', 'albert.einstein', file=f)
        print('password', 'random', file=f)
    with patch.dict(os.environ, NETRC=path):
        yield


def test_login(netrc_mattermost):
    mm = mattermost_api.MMApi("https://chat.ligo.org/api/v4/")
    token = channel_creation.get_auth("mattermost-bot")
    login_response = mm.login(token)
    assert login_response.status_code > 200
    mm.logout()


superevent_dict = {
    "superevent_id": "rrt-package"
}


def test_channel_creation(netrc_mattermost):
    creation_response = channel_creation.rrt_channel_creation(
        superevent_dict)
    assert creation_response.status_code > 200

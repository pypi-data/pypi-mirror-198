from ligo.rrt_chat import mattermost_api
from safe_netrc import netrc, NetrcParseError


def get_auth(host):
    try:
        auth = netrc().authenticators(host)
        if not auth:
            raise ValueError('No netrc entry found for {}'.format(host))
        else:
            _, _, TOKEN = auth
            return TOKEN
    except (NetrcParseError, OSError, ValueError):
        print('Could not load the mattermost bot'
              'token for {} from the netrc file'.format(host))


def rrt_channel_creation(superevent_dict):
    """
    Creates a channel in LIGO team in Mattermost based
    on the superevent_id. Also attaches a link for the
    corresponding gracedb entry.

    Parameters
    ----------
    superevent_dict: dict
        The superevent dictionary containing superevent id
    """
    LIGO_ID = "c1fdk6iyj3b59kn3dakk8iufxo"
    MATTERMOST_API = "https://chat.ligo.org/api/v4/"
    # Mattermost credentials file needs to be changed according to user
    mm = mattermost_api.MMApi(MATTERMOST_API)
    token = get_auth("mattermost-bot")
    login_response = mm.login(bearer=token)
    if login_response.status_code != 200:
        return login_response
    id = superevent_dict["superevent_id"]
    channel_name = "rrt-" + id.lower()
    channel_display_name = "RRT " + id
    # check if the channel already exist
    channel_check = mm.search_channel_by_name(LIGO_ID, channel_name)
    if channel_check.status_code >= 400:
        channel_response = mm.create_channel(LIGO_ID, channel_name,
                                             channel_display_name)
        if channel_response.status_code == 201:
            channel_id = channel_response.json()['id']
            grace_url = "https://gracedb-playground.ligo.org/superevents/" + \
                        id+"/view/"
            mm.post_in_channel(channel_id, grace_url)
            mm.logout()
        else:
            mm.logout()
            return channel_response
    else:
        mm.logout()
        return channel_check

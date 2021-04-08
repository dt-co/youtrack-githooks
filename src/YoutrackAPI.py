import requests
import re

class YoutrackAPI:

    def __init__(self, token, url):
        self.token = token
        self.base_url = url

    @staticmethod
    def set_state(state, type):
        state = state.lower()
        if type == 'pull_request': # https://docs.github.com/en/developers/webhooks-and-events/github-event-types#pullrequestevent
            if state in ['review_requested', 'opened', 'reopened']:
                return "state To Verify"
            if state in ['closed']:
                return "State In Progress"
            if state == 'merged':
                return "state Done"
        if type == 'pull_request_review':
            if state in ['changes_requested']:
                return "State In Progress"
            if state in ['approved']:
                return "state To Verify"
        return 'None'

    def post(self, body):
        headers = {
            "Authorization": "Bearer " + self.token,
            "Accept": "application/json",
            "Content-type": "application/json"
        }
        url = self.base_url + "commands"
        response = requests.request("post", url, headers=headers, json=body)
        if response.status_code == 401:
            raise Exception("Failed to authorize against YouTrack")
        return response

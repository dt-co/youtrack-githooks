import requests
import re

class YoutrackAPI:
    base_url = "https://youtrack.internal.dtco.io/api/commands"

    def __init__(self, token):
        self.token = token

    @staticmethod
    def set_state(state, type):
        state = state.lower()
        if type == 'pull_request':
            if state in ['review_requested', 'ready_for_review', 'opened', 'reopened']:
                return "state To Verify"
            if state in ['converted_to_draft', 'closed']:
                return "State In Progress"
            if state == 'merged':
                return "state Done"
        if type == 'pull_request_review':
            if state in ['request_changes']: #approve
                return "State In Progress"
        return 'None'

    def post(self, body):
        headers = {
            "Authorization": "Bearer " + self.token,
            "Accept": "application/json",
            "Content-type": "application/json"
        }
        url = self.base_url
        response = requests.request("post", url, headers=headers, json=body)
        if response.status_code == 401:
            raise Exception("Failed to authorize against YouTrack")
        return response

import sys
import json
from YoutrackAPI import YoutrackAPI

token = sys.argv[2]
data = json.loads(sys.argv[1])
event_name = data['event_name']
issue = data['event']['pull_request']['head']['ref']
if event_name.lower() == 'pull_request':
    action = data['event']['action']
    merged = data['event']['pull_request']['merged']
    if action.lower() == 'closed' and merged == true:
        action = 'merged'
else:
    action = data['event']['review']['state']

if event_name and action and issue:
    print("Working on branch: {} on state: {}".format(issue, action))

    api = YoutrackAPI(token)
    query = api.set_state(action, event_name)
    if query != 'None':
        params = {
            "query": "{}".format(query),
            "issues": [ { "idReadable": "{}".format(issue) } ]
        }
        print(params)


        result = api.post(params)
        print(result)
    else:
        print('Closed without merging. Ignoring...')
else:
    print('branch or state missing.')

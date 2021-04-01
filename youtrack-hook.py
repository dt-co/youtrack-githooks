import sys
import json
from YoutrackAPI import YoutrackAPI
type = sys.argv[1]
branch = sys.argv[2]
state = sys.argv[3]
if type.lower() == 'pull_request' and state.lower() == 'closed' and sys.argv[4].lower() == 'true':
    state = 'merged'
if branch and state and type:
    token = 'perm:ZGF2aWQudmFuLndlc3RyZWVuZW4=.NTEtMw==.dfzYzK5pbn3HgTUkbqH4RGR3vhmXPT'

    print("Working on branch: {} on state: {}".format(branch, state))

    api = YoutrackAPI(token)
    query = api.set_state(state, type)
    if query != 'None':
        params = {
            "query": "{}".format(api.set_state(state, type)),
            "issues": [ { "idReadable": "{}".format(branch) } ]
        }
        print(params)


#         result = api.post(params)
#         print(result)
    else:
        print('Closed without merging. Ignoring...')
else:
    print('branch or state missing.')


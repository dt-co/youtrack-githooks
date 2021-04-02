import sys
import json
from YoutrackAPI import YoutrackAPI
print(sys.argv[1])
print(sts.argv[2])
# type = sys.argv[1]
# branch = sys.argv[2]
# state = sys.argv[3]
# if type.lower() == 'pull_request' and state.lower() == 'closed' and sys.argv[4].lower() == 'true':
#     state = 'merged'
# if branch and state and type:
#     token = 'perm:ZGF2aWQudmFuLndlc3RyZWVuZW4=.NTEtMw==.dfzYzK5pbn3HgTUkbqH4RGR3vhmXPT'
#
#     print("Working on branch: {} on state: {}".format(branch, state))
#
#     api = YoutrackAPI(token)
#     query = api.set_state(state, type)
#     if query != 'None':
#         params = {
#             "query": "{}".format(api.set_state(state, type)),
#             "issues": [ { "idReadable": "{}".format(branch) } ]
#         }
#         print(params)
#
#
# #         result = api.post(params)
# #         print(result)
#     else:
#         print('Closed without merging. Ignoring...')
# else:
#     print('branch or state missing.')
#
#       - name: Get output
#         run: echo "output is ${{ steps.ytrack.outputs.result }}"
#       - name: Youtrack Pull request
#         if: ${{ github.event_name == 'pull_request' }}
#         run: |
#           echo "$(python youtrack-hook.py '${{ github.event_name }}' '${{ github.event.pull_request.head.ref }}' '${{ github.event.action }}' '${{ github.event.pull_request.merged }}')"
#       - name: Youtrack Review
#         if: ${{ github.event_name == 'pull_request_review' }}
#         run: |
#           echo "$(python youtrack-hook.py '${{ github.event_name }}' '${{ github.event.pull_request.head.ref }}' '${{ github.event.review.state }}')"
#       - name: Debug
#         run: |
#           echo "${{ github.event_name }} ${{ github.event.action }} review state: ${{ github.event.review.state }}"

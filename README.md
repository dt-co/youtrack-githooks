YouTrack github integration

### Make sure you have the next variables
- YOUTRACK_API_KEY (e.g.) <domain>/api/
- YOUTRACK_API_URL 

### Sample code 

```sh 
name: youtrack-ticket
on:
  pull_request:
    types: [review_requested, opened, reopened, closed]
  pull_request_review:
    types: [submitted, dismissed, edited]
jobs:
  move-ticket:
    runs-on: ubuntu-latest
    steps:
      - name: Youtrack issue action
        uses: dt-co/youtrack-githooks@1.1
        env:
          GITHUB_CONTEXT: ${{ tojson(github) }}
          YOUTRACK_API_KEY: ${{ secrets.YOUTRACK_API_KEY }}
          YOUTRACK_API_URL: ${{ secrets.YOUTRACK_API_URL }}
```

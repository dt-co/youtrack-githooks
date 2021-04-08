#!/bin/sh -l


python /youtrack-githooks/youtrack-hook.py "$GITHUB_CONTEXT" "$YOUTRACK_API_KEY" "$YOUTRACK_API_URL"
echo "Bye."

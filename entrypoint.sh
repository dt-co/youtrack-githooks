#!/bin/sh -l

# python ./src/youtrack-hook.py "$1" "$2"
python ./src/youtrack-hook.py "$GITHUB_CONTEXT" "$YOUTRACK_API_KEY"
echo "Hello"
time=$(date)
echo "::set-output name=result::$time"

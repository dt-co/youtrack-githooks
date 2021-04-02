#!/bin/sh -l

python youtrack-hook.py "$1" "$2"
echo "Hello $1"
time=$(date)
echo "::set-output name=result::$time"

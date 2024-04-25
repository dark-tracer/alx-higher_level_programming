#!/bin/bash
# Get thr content-length of a giving ip address
curl -sI "$1" | awk '/Content-Length/{print $2}'

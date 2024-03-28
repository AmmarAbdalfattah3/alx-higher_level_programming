#!/bin/bash
#This bash script sends a DELETE request to the URL passed
curl -sf "$1" -X DELETE

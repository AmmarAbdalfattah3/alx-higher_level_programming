#!/bin/bash
#This bash script sends a DELETE request to the URL passed
curl -sfL "$1" -X DELETE

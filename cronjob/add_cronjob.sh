#!/bin/bash

echo "$(cat weatherbox ; crontab -l)" | crontab -

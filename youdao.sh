#!/bin/bash
# 下载有道的mp3 
# cat words.txt |xargs -t -n 1 youdao.sh
# wget -c "http://dict.youdao.com/dictvoice?audio=$1&type=1" -O "/home/toby/dict/youdao/british/$1.mp3"
if [ ! -e "/home/toby/dict/youdao/american/$1.mp3" ]; then
  wget -c "http://dict.youdao.com/dictvoice?audio=$1&type=2" -O "/home/toby/dict/youdao/american/$1.mp3"
fi

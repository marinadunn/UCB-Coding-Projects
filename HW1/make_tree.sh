#!/bin/bash
chmod +x make_tree.sh
mkdir s1
mkdir s1/s2
mkdir s1/s3
mkdir s1/s2/Advanced

touch s1/s3/conf.txt
echo "I love bash scripting." >> s1/s3/conf.txt

touch s1/s2/text_chunk1.txt
echo "What makes you think she’s a witch?\n Well she turned me into a newt!\n A newt?\n" >> s1/s2/text_chunk1.txt

touch s1/s2/Advanced/text_chunk2.txt
cat s1/s2/text_chunk1.txt > s1/s2/Advanced/text_chunk2.txt
echo "Well I got better..." >> s1/s2/Advanced/text_chunk2.txt


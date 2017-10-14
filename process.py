#!/bin/python
# -*- coding: utf-8 -*-
# post process script for adding comments on html files
import sys


# read html file
if len(sys.argv) < 1:
    print("python process.py <文件名>")
    exit(1)

source = sys.argv[1]
content = ''

with open(source, 'r') as f:
    content = f.read()

# append these lines before "<title>"
scripts = '''
<!-- comment.js -->
<link rel="stylesheet" href="/comment.css"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/0.3.6/marked.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/timeago.js/3.0.2/timeago.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/spin.js/2.3.2/spin.min.js"></script>
<script src="/comment.js"></script>
<style type="text/css">
 #comment-thread {
	 padding-top: 7em;
	 margin-left: 45px;
	 margin-right: 45px;
 }
</style>	
<script type="text/javascript">
 var opt = {
	 type: "github",
	 user: "wzpan",
	 repo: "wzpan.github.io",
	 no_comment: "暂无评价呢",
	 go_to_comment: "去给我评价",
	 issue_id: "11",
	 btn_class: "btn",
	 comments_target: "#comment-thread",
	 client_id: "1eb35434de75c06a513f",
	 client_secret: "6e4193f8ecd619cdfac2b1aa16b3663fe18d2e90"
 };
 getComments(opt);
</script>
<title></title>
'''

content = content.replace('<title></title>', scripts)

# append this line to the end of <div class="pc pc3 w0 h0">
comment = '''
<div id="comment-thread"></div>
'''

content = content.replace('你认识我吗？给我发表评价吧<span class="ffc">.</span></div>', '你认识我吗？给我发表评价吧<span class="ffc">.</span></div>' + comment)

content = content.replace('Do you know me? Please comment on me<span class="ffc">.</span></div>', '你认识我吗？给我发表评价吧<span class="ffc">.</span></div>' + comment)

with open(source, 'w') as f:
    f.write(content)

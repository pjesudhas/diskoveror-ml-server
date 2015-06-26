'''
Copyright 2015 Serendio Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
'''
__author__ = "Satish Palaniappan"

from twokenize import *

Code  = r"\\[a-zA-Z0-9]+"
ReList = [
    Url_RE,
    Entity,
    Timelike,
    NumNum,
    NumberWithCommas,
    Code,
    Punct,
    Separators,
    Decorations
]

stoplist = [")","(",".","'",",",";",":","?","/","!","@","$","*","+","-","_","=","&","%","`","~","\"","{","}"]


def prep (text):
	line = text
	for r in ["@","#"]:
		line = line.lower().replace(r," ")
	for w in stoplist:
		line = line.replace(w," ")
	return line

def aggresivePreproces (text):
	line = text.decode("utf-8")
	for ree in ReList:
		line = re.sub(ree,"", str(line.strip()))
	return line
def process(text):
	text = str(text.strip()).encode("utf-8")
	text = aggresivePreproces(text)
	text = prep(text)
	text =u" ".join(tokenize(text))
	return text.decode("utf-8")

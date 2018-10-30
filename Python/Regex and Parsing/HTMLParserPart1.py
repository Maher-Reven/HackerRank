from html.parser import HTMLParser
n = int(input().strip())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if len(attrs) > 0:
            for x in range(len(attrs)): 
                if len(attrs[x]) < 1:
                    continue
                elif len(attrs[x]) > 1:
                    if attrs[x][1]!="":
                        print("->", attrs[x][0], ">", attrs[x][1])
                    else:
                        print("->", attrs[x][0], ">", "None")
                
    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_comment(self, data):
        pass

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if len(attrs) > 0:
            for x in range(len(attrs)): 
                if len(attrs[x]) < 1:
                    continue
                elif len(attrs[x]) > 1:
                    if attrs[x][1]!="":
                        print("->", attrs[x][0], ">", attrs[x][1])
                    else:
                        print("->", attrs[x][0], ">", "None")

parser = MyHTMLParser()
code = [input().strip() for _ in range(n)]
for y in code:
    parser.feed(y)
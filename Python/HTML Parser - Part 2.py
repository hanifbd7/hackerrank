        def handle_starttag(self, tag, attrs):
            #print("Start : "+tag)
            #for e in attrs: print("-> "+e[0]+" > "+str(e[1]))
            pass
        def handle_endtag(self, tag):
            #print("End   : "+tag)
            pass
        def handle_startendtag(self, tag, attrs):
            #print("Empty : "+tag)
            #for e in attrs: print("-> "+e[0]+" > "+str(e[1]))
            pass
        def handle_comment(self, data):
            #something is completely broken here
            print(">>> Multi-line Comment" if "\n" in data else ">>> Single-line Comment")
            print(data.replace("\r","\n"))
        def handle_data(self, data):
            if data.strip():
                print(">>> Data")
                print(data)

    def handle_starttag(self, tag, attrs):
        print tag
        for attr, value in attrs:
            print "->", attr, ">", value

    def handle_startendtag(self, tag, attrs):
        print tag
        for attr, value in attrs:
            print "->", attr, ">", value

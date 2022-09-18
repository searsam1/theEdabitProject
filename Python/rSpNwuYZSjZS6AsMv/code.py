import re

def imgurUrlParser(url):
	p = r"(?:/)(\w+)"
	id_ = re.findall(p,url)[0]
	
	if "/a/" in url:
		return {'id' : id_, 'type' : 'album'}
	if "/gallery/" in url:
		return {'id' : id_, 'type' : 'gallery'}
	if "//i" in url:
		return {'id' : id_, 'type' : 'image'}
		

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

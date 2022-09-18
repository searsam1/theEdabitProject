def imgurUrlParser(url):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsole# Base tests
Test.assert_equals(
	imgurUrlParser('http://imgur.com/a/IgkdN'),
	{ 'id': 'IgkdN', 'type': 'album' },
	'Should work with an album'
)
Test.assert_equals(
	imgurUrlParser('http://imgur.com/gallery/59npG'),
	{ 'id': '59npG', 'type': 'gallery' },
	'Should work with a gallery'
)
Test.assert_equals(
	imgurUrlParser('http://imgur.com/OzZUNMM'),
	{ 'id': 'OzZUNMM', 'type': 'image' },
	'Should work with a single image'
)
Test.assert_equals(
	imgurUrlParser('http://i.imgur.com/0vrCOSe.jpg'),
	{ 'id': '0vrCOSe', 'type': 'image' },
	'Should work with a single image (direct link)'
)

# Additional tests
Test.assert_equals(
	imgurUrlParser('http://imgur.com/a/cjh4E/zip'),
	{ 'id': 'cjh4E', 'type': 'album' },
	'Should work with /zip at the end (Yeah it\'s a real thing!)'
)
Test.assert_equals(
	imgurUrlParser('http://imgur.com/gallery/jSOZz#Qo9NCpp'),
	{ 'id': 'jSOZz', 'type': 'gallery' },
	'Should work with a #hash at the end'
)
Test.assert_equals(
	imgurUrlParser('www.i.imgur.com/VJ78GRk.jpg'),
	{ 'id': 'VJ78GRk', 'type': 'image' },
	'Should work with www. instead of http://'
)
Test.assert_equals(
	imgurUrlParser('i.imgur.com/d2Ns8nw.png'),
	{ 'id': 'd2Ns8nw', 'type': 'image' },
	'Should work without http:// and www.'
)
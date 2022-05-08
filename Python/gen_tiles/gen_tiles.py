def gen_tiles():
	suits = ["tong", "tiao", "wan"]
	ranks = ["yi", "er", "san" ,"si","wu","liu","qi","ba","jiu"]
	tiles = []

	d = {
		"yi tong" : "bing gan",
		"er tong" : "yan jing",
		"yi tiao" : "ji",
	}

	for rank in ranks:
		t = [rank + " " + suit for suit in suits for _ in range(4)]
		
		tiles = [i if not i in ["yi tong", "er tong","yi tiao"]
			else d[i] for i in tiles 
				]
		tiles += t
	return tiles



gen_tiles()

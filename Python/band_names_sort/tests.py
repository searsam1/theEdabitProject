from band_names_sort import band_names_sort
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  \n\n")
		checks.append(["Fail","Pass"][a==b])
		print("\n")
		print(checks)

band_names = [["The Plot in You", "The Devil Wears Prada", "Pierce the Veil", "Norma Jean", "The Bled", "Say Anything", "The Midway State", "We Came as Romans", "Counterparts", "Oh, Sleeper", "A Skylit Drive", "Anywhere But Here", "An Old Dog"],
		['The New Yardbirds', 'The Beatles', 'The Square Roots', 'On A Friday', 'An Irony'], 
		['The Platters', 'A Yard of Yarn', 'The Everly Brothers', 'A Monster Effect', 'The Sex Maggots'], 
		['But Myth', 'An Old Dog', 'Def Leppard', 'The Any Glitters', 'The Dawn'], 
		['Van Halen', 'The Beastie Boys', 'Radiohead', 'The Gamma Ray', 'Led Zeppelin'], 
		['The Young Guns', 'The Fugees', 'Coldplay', 'The Grateful Dead', 'The Artistics'],
		['The Old American Rejects', 'The Cure', 'The Who', 'Goo Goo Dolls', 'The Bee Gees']]
		
sorted_bands = [["Anywhere But Here", "The Bled", "Counterparts", "The Devil Wears Prada", "The Midway State", "Norma Jean", "Oh, Sleeper", "An Old Dog", "Pierce the Veil", "The Plot in You", "Say Anything", "A Skylit Drive", "We Came as Romans"], 
		['The Beatles', 'An Irony', 'The New Yardbirds', 'On A Friday', 'The Square Roots'],
		['The Everly Brothers', 'A Monster Effect', 'The Platters', 'The Sex Maggots', 'A Yard of Yarn'],
		['The Any Glitters', 'But Myth', 'The Dawn', 'Def Leppard', 'An Old Dog'],
		['The Beastie Boys', 'The Gamma Ray', 'Led Zeppelin', 'Radiohead', 'Van Halen'],
		['The Artistics', 'Coldplay', 'The Fugees', 'The Grateful Dead', 'The Young Guns'],
		['The Bee Gees', 'The Cure', 'Goo Goo Dolls', 'The Old American Rejects', 'The Who']]

for i, n in enumerate(band_names):
	Test.assert_equals(band_names_sort(n), sorted_bands[i])

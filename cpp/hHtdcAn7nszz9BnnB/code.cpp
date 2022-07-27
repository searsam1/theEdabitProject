
std::string mdFormat(std::string word, char style) {
	if (style == 'b'){
	  return "**" + word + "**";
	}
  	if (style == 'i'){
	  return '_' + word + '_';
	}
  	if (style == 'c'){
	  return '`' + word + '`';
	}
  	if (style == 's'){
	  return "~~" + word + "~~";
	}
  return word;
}
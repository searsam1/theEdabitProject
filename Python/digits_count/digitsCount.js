function digitsCount(n) {
  total = 1;
  n = Math.abs(n);
  while (n > 10){
	 n /= 10;
	 total += 1;
    }
  return total;
}
# Odd Up, Even Down — N Times
## Published by Helen Yu in C++

Create a function that performs an even-odd transform to an array, n times. Each even-odd transformation:
Adds two (+2) to each odd integer.
Subtracts two (-2) from each even integer.

## Examples

``` 
evenOddTransform([3, 4, 9], 3) ➞ [9, -2, 15]
// Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]

evenOddTransform([0, 0, 0], 10) ➞ [-20, -20, -20]

evenOddTransform([1, 2, 3], 1) ➞ [3, 0, 5]
```

## Notes

N/A

# Solution 
```
std::vector<int> evenOddTransform(std::vector<int> arr, int n) {
	std::vector<int> res;
  	
  	for (int i=0; i<n; ++i)
	{
		for (int i : arr)
	  {
		if (i % 2)
		{
		  res.push_back(i + 2);
		}
		else 
		{
		  res.push_back(i - 2);
		}
	  }
	  arr = res;
	  res.clear();
	}

  	return arr;
}
```
# EOF

#include "vector"
#include "iostream"
#include <algorithm>

using namespace std;
using std::vector;

vector<int> twoSum(vector<int> nums, int target) {
        vector<int> sol;
        int temp, i = 0, l = nums.size();
        while(i < l)
        {
            temp = nums[i] - target;
           int it = nums.end() - find(nums.begin(), nums.end(), temp);
            if(it == 0)
            {   i++;
                continue;
            }
            sol[0] = i;
            sol[1] = it;
            break;
        }
     return sol;   
    }

int main(int argc, char const *argv[])
{
    vector<int> v = {1,2,3,4};

    for (int i : twoSum{v, 4})
    {
        cout << i;
    }

    
}
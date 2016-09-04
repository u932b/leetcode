# include <iostream>
# include <vector>
using namespace std;

int getSum(int &a, int &b){
    int and_res = (a & b) << 1;
    int xor_res = a ^ b;
    while (and_res != 0){
        int old_and_res = and_res;
        and_res = (and_res & xor_res) << 1;
        xor_res = old_and_res ^ xor_res;
    }
    return xor_res;

}

struct testCase{
    vector<pair<int, int> > test_cases;
    void test_result(){
        for (int i=0; i<test_cases.size(); i++){
            int first = test_cases[i].first;
            int second = test_cases[i].second;
            printf("Number to be added: %d, %d \n", first, second);
            int expected = first + second;
            int result = getSum(first, second);
            if (result != expected){
                cout << "WRONG !!!! ";
            }else{
                cout << "GOOD ";
            }
            cout << "Expected: " << first + second << " Result of addition: " << getSum(first, second) << endl << endl;
        }
    }

};

int main(){
    testCase ts1;
    ts1.test_cases.push_back(make_pair(1,2));
    ts1.test_cases.push_back(make_pair(10,2));
    ts1.test_cases.push_back(make_pair(10,12));
    ts1.test_cases.push_back(make_pair(10,999));
    ts1.test_cases.push_back(make_pair(10,14));
    ts1.test_result();
    return 0;
}

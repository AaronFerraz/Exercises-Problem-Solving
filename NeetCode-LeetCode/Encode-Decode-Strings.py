''' 
Properties
Title: Group Anagrams
Level: Medium

Statement:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is 
decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}

Machine 2 (receiver) has the function:
vector<string> decode(string s) {
    //... your code
    return strs;
}

So Machine 1 does:
string encoded_string = encode(strs);

and Machine 2 does:
vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.
Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:
Input: dummy_input = [""]
Output: [""]
'''


from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            delimiter_index = s.find('#', i)
            length = int(s[i:delimiter_index])
            start = delimiter_index + 1
            end = start + length
            decoded_list.append(s[start:end])
            i = end
        return decoded_list


# Tests
solver = Solution()

teste1 = solver.encode(['Hello', 'World'])
print(f"Input: ['Hello', 'World'] - Output: {solver.decode(teste1)}")

teste2 = solver.encode([""])
print(f"Input: [''] - Output: {solver.decode(teste2)}")
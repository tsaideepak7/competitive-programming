class node:
    def __init__(self):
        self.children = {}
        self.isend = False
        self.value = 0

class Trie:
    def __init__(self):
        self.root = node()

    def insert(self, word, num):
        curr = trie.root
        for bit in word:
            if bit not in curr.children:
                curr.children[bit] = node()
            curr = curr.children[bit]
        curr.isend = True
        curr.value = num

    def search(self, word, num):
        curr = trie.root
        for bit in word:
            if bit == '1' and curr.children.get('0'):
                curr = curr.children['0']
            elif bit == '0' and curr.children.get('1'):
                curr = curr.children['1']
            else:
                curr = curr.children[bit]

        return num^curr.value

    
nums=map(int,input().split())
trie = Trie()
max_xor = -2**32

for num in nums:
    num_bin = (bin(num)[2:]).zfill(31) #string, max = 31bits
    print(num,num_bin)
    trie.insert(num_bin , num)
    max_xor = max(max_xor,trie.search(num_bin,num))
'''
for num in nums:
    num_bin = (bin(num)[2:]).zfill(31)
    print(trie.search(num_bin,num))
'''

print(max_xor)


    
    

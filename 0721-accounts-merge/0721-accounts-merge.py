from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x
        
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_list_size = len(accounts)
        uf = UnionFind(account_list_size)
        
        email_group = {}
        for i in range(account_list_size):
            account_size = len(accounts[i])
            
            for j in range(1, account_size):
                email = accounts[i][j]
                
                # if we have not seen this email, create a new group for it
                if email not in email_group:
                    email_group[email] = i
                else:
                    # we have seen this email, union this group with the previous email
                    uf.union(i, email_group[email])
            
        components = defaultdict(list)
        for email,group in email_group.items():
            components[uf.find(group)].append(email)
        
        merged_accounts = []
        for group,emails in components.items():
            name = accounts[group][0]
            merged_accounts.append([name] + sorted(emails))
        
        return merged_accounts
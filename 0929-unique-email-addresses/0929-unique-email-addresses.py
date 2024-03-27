class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        receive_mails = set()
        
        for email in emails:
            
            local, domain = email.split("@")
            filtered = local.split("+")[0].split(".")
            
            valid_email = "".join(filtered) + "@" + domain
            
            receive_mails.add(valid_email)
            
        
        
        return len(receive_mails)
        
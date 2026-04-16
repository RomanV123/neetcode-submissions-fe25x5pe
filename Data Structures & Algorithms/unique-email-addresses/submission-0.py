class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        clean_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', "")
            local = local.split('+')[0]
            cleaned_email = local + domain
            clean_emails.add(cleaned_email)

        return len(clean_emails)





        
class Page:
    def __init__(self, heading, body):
        self.heading = heading
        self.body = body
    def create_page(self):
        html = f"<h1>{self.heading}</h1> <p>{self.body}</p>"
        return html
    
class Contact(Page):
    def __init__(self, heading, body, email):
        super().__init__(heading, body)
        self.email = email
contact_page = Contact("Contact us", "Please give us your feedback", "abc@gmail.com")
print(contact_page.heading)


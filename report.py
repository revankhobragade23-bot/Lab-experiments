def report_format(func):
    def wrapper(report):
        print("\n" + "=" * 40)
        print("  DYNAMIC REPORT")
        print("=" * 40)
        func(report)
        print("=" * 40)
    return wrapper 

class report:
    template = "simple"

    def __init__(self, title, content):
        self.title = title
        self.content = content 

    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    def __str__(self):
        return (
            f"title : {self.title}\n"
            f"content : {self.content}\n"
            f"template : {report.template}\n"
        )        

@report_format
def display(report):
    print(report)

# Main Program #

print("choose report template")
print("1. simple")
print("2. professional")
print("3. modern")

choice = input("enter your choice: ")

if choice == "1":
    report.change_template("simple")
elif choice == "2":
    report.change_template("professional")
elif choice == "3":
    report.change_template("modern")
else:
    print("invalid choice! default template will be used.") 

title = input("\nEnter report title: ")
content = input("Enter report content:")

Report = report(title, content)

display(Report)
        


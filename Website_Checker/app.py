print("Website URL Checker")

url=input("Enter a website URL: ")

if url.startswith("https://"):
    print("This website uses HTTPS (Secure)")
elif url.startswith("http://"):
    print("This website uses HTTP (not secure)")
else:
    print("This doesn't look like a complete URL")
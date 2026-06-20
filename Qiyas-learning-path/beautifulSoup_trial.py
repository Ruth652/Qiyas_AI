from bs4 import BeautifulSoup

html = """
<html>
    <body>

        <h1>Python Web Scraping</h1>

        <p>This is the first paragraph.</p>

        <p>This is the second paragraph.</p>

        <a href="https://google.com">Google</a>

    </body>
</html>
"""

# PARSE THE HTML, CREATE A BEAUTIFULSOUP OBJECT
soup = BeautifulSoup(html, "html.parser")

# =====================================================
# STEP 3: PRINT THE ENTIRE HTML
# =====================================================

print("FULL HTML")
print(soup)

# FIND THE FIRST H1 TAG
heading = soup.find("h1")

print("\nFIRST H1 TAG")
print(heading)

# GET ONLY THE TEXT INSIDE H1

print("\nTEXT INSIDE H1")
print(heading.text)


#  FIND THE FIRST PARAGRAPH


paragraph = soup.find("p")

print("\nFIRST PARAGRAPH")
print(paragraph)

print("\nFIRST PARAGRAPH TEXT")
print(paragraph.text)

# FIND ALL PARAGRAPHS

paragraphs = soup.find_all("p")

print("\nALL PARAGRAPHS")

for p in paragraphs:
    print(p.text)

# FIND A LINK

link = soup.find("a")

print("\nLINK TAG")
print(link)

print("\nLINK TEXT")
print(link.text)

# GET THE HREF ATTRIBUTE

print("\nLINK URL")
print(link["href"])
# Bookmark Crawler - Crawl Individual Sites
---

Give person a URL
They open the webpage
Click on all of the links
Take all of the links and titles and compile them into a list
Take that list and turn it into a pretty HTML file

---

### Full Program
Input Type - URL as a string
Output Type - HTML file

---

The person will start by asking for an URL.
The user will type in the URL so the person has it.
The person will take the URL and open it so it can read it
The person will open all of the links on the page.
The person will take all of the opened links and titles and put them in a list.
The person will take this new list of found URLs and add them to an HTML file.

---

def INPUT:
	Asks the user for a URL

def CRAWLER:
	Take the URL and open it so it can read it
	Open all of the links on the page
	Take all of the opened links and titles and put them in a list

def OUTPUT:
	Take this new list of found URLs and add them to an HTML file

---

### INPUT:
* Input type: string of URL
* Output type: list of tuples containing URL, title, and source

### CRAWLER:
* Input type: list of tuples containing URL, title, and source
* Output type: list of tuples containing URL, title, and source

### OUTPUT:
* Input type: list of tuples containing URL, title, and source
* Output type: HTML file of all links
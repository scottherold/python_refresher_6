import webbrowser

# webbrowser.open("https://www.python.org/")

chrome = webbrowser.get(using='google-chrome')
chrome.open_new_tab("https://www.python.org/")
import webbrowser

#print(dir(webbrowser))

#help(webbrowser)

webbrowser.get()

webbrowser.open('http://www.bbc.co.uk')

#webbrowser.open_new_tab('https://google.com')

chrome = webbrowser.get(using='google-chrome')

chrome.open('http://www.foo.com')
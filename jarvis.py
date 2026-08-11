import os
import webbrowser

print("Jarvis activating workspace...")

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

try:
    browser = webbrowser.get(chrome_path)
    browser.open("https://gemini.google.com")
    browser.open("https://www.youtube.com/results?search_query=lofi+music")
except Exception:
    webbrowser.open("https://gemini.google.com")
    webbrowser.open("https://www.youtube.com/results?search_query=lofi+music")

try:
    os.system("start /b code")
    print("Opening VS Code...")
except Exception:
    print("Failed to open VS Code.")

print("All done!")
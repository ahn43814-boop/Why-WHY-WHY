import webbrowser
import time
import sys

def force_browser_open(url, interval_seconds):
    """
    Continuously opens a web browser to a specified URL at a given interval.

    Args:
        url (str): The URL to open in the browser.
        interval_seconds (int): The time in seconds to wait between opening the browser.
    """
    try:
        while True:
            webbrowser.open(url)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("Operation stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    target_url = "https://shrinkme.click/Ug4mPEm"
    open_interval = 25
    force_browser_open(target_url, open_interval)

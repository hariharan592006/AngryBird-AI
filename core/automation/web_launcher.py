import webbrowser

from core.automation.websites import WEBSITES


class WebLauncher:

    def launch(self, website: str):

        website = website.lower()

        url = WEBSITES.get(website)

        if not url:
            return f"I couldn't find {website}."

        webbrowser.open(url)

        return f"Opening {website.title()}..."
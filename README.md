# DrHouseDownloader

This Python script scrapes links from multiple web pages and generates a Bash script for downloading files using the `aria2c` command-line tool. It is specifically designed to download episodes from the TV series "House M.D." from the website Nollyverse (https://www.nollyverse.com/serie/).

## Prerequisites

- Python 3.x
- `requests` library
- `BeautifulSoup` library

## Usage

1. Clone the repository or download the script file.

2. Install the required Python libraries:

   ```bash
   pip install requests beautifulsoup4
3. Modify the script (if needed):
- If you want to scrape links from different web pages for different TV Shows, update the URLS list with the desired URLs.
- Adjust the BTN_CLASS if the class name of the buttons containing the links is different.
- Customize the PREFIX with your own aria2c options or remove the proxy configuration.
- Optionally, change the OUTPUT_PATH to specify a different file path for the generated Bash script.

4. Run the script:
   ```bash
   python script.py
   ```
The generated Bash script will be saved in the specified OUTPUT_PATH file.

5. Change the permissions of the file by executing:
   ```bash
   chmod +x DrHouseDownloader.sh
   ```
6. Execute the generated Bash script to start downloading the files:
   ```bash
   ./DrHouseDownloader.sh
   ```
or
   ```bash
   bash DrHouseDownloader.sh
   ```
7. The script will use aria2c to download the files in parallel with the specified options.

## Important Notes
- Ensure that you have permission to scrape the websites you're targeting and comply with any applicable terms of service and legal restrictions.
- Verify that you have a working internet connection before running the script.
- Make sure you have sufficient disk space available for the downloaded files.
- This script assumes that you have aria2c installed and available in your system's PATH. If it's not installed, please install it before running the script.
- Please note that the script may not work if the website's structure or class names change. Adjust the script accordingly if needed.

## Contact

If you have any questions, feel free to reach out:

- [Email](mailto:eliser.santiesteban.1996@gmail.com)
- [Twitter](https://twitter.com/hackroot231)

import re
import os


def analyze_log_file(filename="access.log"):
    """Analyzes a log file and extracts information.

    **Instructions:**
    1. Complete the `extract_log_data` function to extract timestamp, IP address, URL, and status code from each valid log line.
    2. (Optional) Implement the `count_status_codes` function to count occurrences of each status code.

    This function opens the log file, reads each line, and performs analysis based on the extracted data.
    """

    try:
        with open(filename, 'r') as file:
            log_lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: Log file '{filename}' not found.")
        return

    error_count = 0
    unique_ips = set()
    url_counts = {}

    for line in log_lines:
        timestamp, ip, url, status_code = extract_log_data(line)
        if timestamp and ip and url and status_code:
            unique_ips.add(ip)

            if url in url_counts:
                url_counts[url] += 1
            else:
                url_counts[url] = 1

            if int(status_code) >= 400:
                error_count += 1

    print(f"Total Errors (4xx and 5xx): {error_count}")
    print(f"Unique IP Addresses: {len(unique_ips)}")
    print("URL Access Counts:")
    for url, count in url_counts.items():
        print(f"    {url}: {count}")


def extract_log_data(line):
    #please note that you do not need to edit this function, just the analyze_log_file function above!
    #example usage: timestamp, ip, url, status_code = extract_log_data(line)
    
    
    """Extracts timestamp, IP address, URL, and status code from a valid log line.

    **Instructions:**
    1. Use regular expressions (re module) to extract the data from the log line format:
       - Timestamp (YYYY-MM-DD HH:MM:SS)
       - IP address (e.g., 192.168.1.1)
       - URL (everything after "GET ")
       - Status code (e.g., 200, 404)
    2. Return a tuple containing the extracted data (timestamp, ip, url, status_code)
    3. If the line format is invalid, return None for all data points.

    **Example Regular Expression:**
    ```python
    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \"GET (.+) HTTP/1.1\" (\d+)", line)
    ```

   """

    match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \"GET (.+) HTTP/1.1\" (\d+)", line)
    if match:
        timestamp, ip, url, status_code = match.groups()
        return timestamp, ip, url, status_code
    else:
        return None, None, None, None



# Generate a sample log file (uncomment to create the file)
# generate_log_file()

# Analyze the log file
analyze_log_file()
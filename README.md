# Simple Battery Monitoring Script

This is a basic Python script for monitoring laptop battery life over time. It's designed for quick, informal battery tests.

## What it does

- Logs battery percentage every minute
- Records elapsed time
- Saves data to a text file

## How to use

1. Start the script:

   ```bash
   python battery_monitor.py
   ```

2. Run your battery test (e.g., play a long YouTube video)
3. Let it run until the battery depletes or you're done testing
4. Check the log file for results

## Requirements

- Python 3.x
- The script will try to install the required `psutil` library automatically

## Notes

- This is a simple, quick solution. There are more robust options available for professional testing.
- The script overwrites the log file each run. Save previous logs if needed.
- Supports English and Brazilian Portuguese (auto-detects system language)

## Example use case

"I usually play a 10-hour Crab Rave video on YouTube and let this script run in the background to see how long the battery lasts."

That's it! Happy testing!

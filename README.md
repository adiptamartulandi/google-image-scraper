# Google Image Scraper

A Python script that allows you to download images from Google Images using the SerpAPI service. This tool makes it easy to collect image datasets for various purposes.

## Features

- Search and download images from Google Images
- Automatically create folders for each search query
- Customizable number of images to download
- Proper error handling and progress tracking
- Supports various image formats (jpg, png, gif, webp)

## Prerequisites

- Python 3.x
- SerpAPI key (Get one at [https://serpapi.com](https://serpapi.com))

## Installation

1. Clone this repository or download the source code

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```bash
python scraper.py
```

The script will prompt you for:
1. Your SerpAPI key
2. Search keyword
3. Number of images to download (default is 10)

The images will be downloaded to a new folder named after your search keyword (spaces replaced with underscores).

### Example

```bash
Enter your SerpAPI key: your_api_key_here
Enter search keyword: cute cats
Enter number of images to download (default 10): 20
```

This will:
1. Create a folder named `cute_cats`
2. Download up to 20 images from Google Images
3. Save them as `image_1.jpg`, `image_2.jpg`, etc.

## Important Notes

- You need a SerpAPI key to use this script. Sign up at [https://serpapi.com](https://serpapi.com)
- The script respects rate limits and includes error handling
- Some images might fail to download due to various reasons (404 errors, timeout, etc.)
- The script automatically handles different image formats

## Dependencies

- requests: For downloading images
- google-search-results: Official SerpAPI client
- serpapi: Additional SerpAPI utilities

## License

This project is open source and available under the MIT License.
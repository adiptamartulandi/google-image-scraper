import os
import requests
from serpapi import GoogleSearch

def create_folder(keyword):
    """Create a folder for storing images if it doesn't exist"""
    folder_name = keyword.replace(' ', '_')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def download_image(url, folder_name, counter):
    """Download image from URL and save it to the specified folder"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Extract file extension from URL or default to .jpg
            file_extension = os.path.splitext(url)[1]
            if not file_extension or len(file_extension) > 5:
                file_extension = '.jpg'
            
            # Save the image
            file_path = os.path.join(folder_name, f'image_{counter}{file_extension}')
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"Error downloading image {url}: {str(e)}")
    return False

def scrape_google_images(keyword, num_images=10, api_key=None):
    """Scrape Google Images based on keyword and download specified number of images using SerpAPI"""
    if not api_key:
        raise ValueError("SerpAPI key is required. Please provide your API key.")

    # Create folder for storing images
    folder_name = create_folder(keyword)
    
    # Prepare the search parameters
    params = {
        "q": keyword,
        "engine": "google_images",
        "ijn": "0",
        "api_key": api_key
    }
    
    try:
        # Perform the search using SerpAPI
        search = GoogleSearch(params)
        results = search.get_dict()
        
        if "error" in results:
            raise Exception(f"SerpAPI error: {results['error']}")
        
        if "images_results" not in results:
            raise Exception("No images found in the search results")
        
        images_results = results["images_results"]
        
        # Download images
        downloaded_count = 0
        for idx, image in enumerate(images_results):
            if downloaded_count >= num_images:
                break
            
            if download_image(image['original'], folder_name, downloaded_count + 1):
                downloaded_count += 1
                print(f'Downloaded image {downloaded_count}/{num_images}')
                
    except Exception as e:
        print(f"Error during scraping: {str(e)}")
    
    print(f"\nDownloaded {downloaded_count} images for keyword: {keyword}")

def main():
    api_key = input("Enter your SerpAPI key: ")
    keyword = input("Enter search keyword: ")
    num_images = int(input("Enter number of images to download (default 10): ") or 10)
    scrape_google_images(keyword, num_images, api_key)

if __name__ == '__main__':
    main()
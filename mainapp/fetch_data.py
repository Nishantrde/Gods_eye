from googleapiclient.discovery import build

# Set up your API key and YouTube service
API_KEY = "AIzaSyAvyvfXLKnNNyyDncBqA7OP14pVuEDRbIo"  # Replace with your YouTube Data API key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Mapping of region codes to country names
REGION_COUNTRY_MAP = {
    "US": "United States", "IN": "India", "JP": "Japan", "BR": "Brazil", "FR": "France", "DE": "Germany",
    "GB": "United Kingdom", "KR": "South Korea", "MX": "Mexico", "CA": "Canada", "AU": "Australia",
    "AR": "Argentina", "ZA": "South Africa", "AE": "United Arab Emirates", "RU": "Russia", "IT": "Italy",
    "ES": "Spain", "NL": "Netherlands", "SE": "Sweden", "CH": "Switzerland", "BE": "Belgium", "TR": "Turkey",
    "ID": "Indonesia", "TH": "Thailand", "PH": "Philippines", "MY": "Malaysia", "SG": "Singapore",
    "HK": "Hong Kong", "TW": "Taiwan", "VN": "Vietnam", "NG": "Nigeria", "EG": "Egypt", "PK": "Pakistan",
    "BD": "Bangladesh", "PL": "Poland", "GR": "Greece", "CZ": "Czech Republic", "AT": "Austria",
    "DK": "Denmark", "FI": "Finland", "IE": "Ireland", "NO": "Norway", "NZ": "New Zealand", "IL": "Israel",
    "HU": "Hungary", "PT": "Portugal", "RO": "Romania", "SA": "Saudi Arabia", "CO": "Colombia",
    "CL": "Chile", "PE": "Peru", "VE": "Venezuela", "UA": "Ukraine", "SK": "Slovakia", "BG": "Bulgaria",
    "HR": "Croatia", "SI": "Slovenia", "LV": "Latvia", "LT": "Lithuania", "EE": "Estonia", "LU": "Luxembourg",
    "MT": "Malta", "CY": "Cyprus", "IS": "Iceland", "CR": "Costa Rica", "DO": "Dominican Republic",
    "GT": "Guatemala", "HN": "Honduras", "NI": "Nicaragua", "PA": "Panama", "SV": "El Salvador",
    "BO": "Bolivia", "PY": "Paraguay", "UY": "Uruguay", "QA": "Qatar", "KW": "Kuwait", "OM": "Oman",
    "BH": "Bahrain", "LB": "Lebanon", "JO": "Jordan", "PS": "Palestine", "MU": "Mauritius", "GH": "Ghana",
    "TZ": "Tanzania", "UG": "Uganda", "ZM": "Zambia", "ZW": "Zimbabwe"
}

def get_number_one_trending_video(youtube, region_code):
    """
    Fetch the #1 trending video for a specific region.
    """
    try:
        request = youtube.videos().list(
            part="snippet,statistics",
            chart="mostPopular",
            regionCode=region_code,
            maxResults=1  # Limit to the top video only
        )
        response = request.execute()
        if "items" in response and len(response["items"]) > 0:
            video = response["items"][0]
            return {
                "title": video["snippet"]["title"],
                "channel": video["snippet"]["channelTitle"],
                "views": int(video["statistics"].get("viewCount", 0)),
                "likes": int(video["statistics"].get("likeCount", 0)),
                "thumbnail": video["snippet"]["thumbnails"]["high"]["url"],  # High-resolution thumbnail URL
                "region": region_code
            }
    except Exception as e:
        print(f"Error fetching trending video for {region_code}: {e}")
    return None

def main():
    data = {}
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    trending_videos = []

    # Fetch the #1 trending video for each region
    for region_code in REGION_COUNTRY_MAP.keys():
        print(f"Fetching #1 trending video for region: {region_code}")
        video = get_number_one_trending_video(youtube, region_code)
        if video:
            trending_videos.append(video)

    # Print the #1 trending video for each region
    print("\n#1 Trending Videos Globally:\n")
    

    for video in trending_videos:
        country_name = REGION_COUNTRY_MAP.get(video['region'], "Unknown Country")
        print(f"{country_name} [{video['region']}]: {video['title']} by {video['channel']} - {video['views']} views, {video['likes']} likes")
        print(f"Thumbnail: {video['thumbnail']}\n")
        data[video['region']] = [video['title'], video['views'], video['likes'], video['thumbnail']]

    return data

if __name__ == "__main__":
    main()

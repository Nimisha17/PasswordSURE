import instaloader

def scrape_instagram_profile(username_to_scrape, your_username, your_password):
    
    L = instaloader.Instaloader()

    try:
        print("  Logging in...")
        L.login(your_username, your_password)
        print(" Login successful.")
    except Exception as e:
        print(" Login failed:", e)
        return

    try:
        profile = instaloader.Profile.from_username(L.context, username_to_scrape)

        print(f"\n  Profile Info for @{username_to_scrape}")
        print(f"Full Name: {profile.full_name}")
        print(f"Username: {profile.username}")
        print(f"Bio: {profile.biography}")
        print(f"External URL: {profile.external_url}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Is Private: {profile.is_private}")
        print(f"Number of Posts: {profile.mediacount}")

        if profile.is_private:
            print("  This account is private. Posts cannot be accessed.")
            return

        print("\n Recent Captions:")
        posts = profile.get_posts()
        for i, post in enumerate(posts):
            if i >= 5:
                break
            print(f"\nPost {i+1}:")
            print(f"Caption: {post.caption}")
            print(f"Hashtags: {[tag for tag in post.caption_hashtags]}")
            print(f"Mentions: {[mention for mention in post.caption_mentions]}")

    except Exception as e:
        print("Error fetching profile:", e)

scrape_instagram_profile(
    username_to_scrape="kyliejenner",         
    your_username="beautifulsoupai",         
    your_password="nimbhargsam25"         )


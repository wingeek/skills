#!/usr/bin/env python3
"""
WeChat Official Account Article Publisher

This script publishes articles to WeChat via API.
Usage: python publish_wechat.py --article article.html --title "Title" --cover cover.jpg
"""

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Dict, Optional

import requests


class WeChatPublisher:
    """WeChat Official Account Publisher"""

    def __init__(self, app_id: str, app_secret: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self.token: Optional[str] = None
        self.token_expires_at: float = 0

    def get_access_token(self) -> str:
        """Get or refresh access token"""
        # Check if token is still valid (with 5 min buffer)
        if self.token and time.time() < self.token_expires_at:
            return self.token

        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": self.app_id,
            "secret": self.app_secret
        }

        print("🔑 Getting access token...")
        response = requests.get(url, params=params)
        data = response.json()

        if "access_token" not in data:
            print(f"❌ Failed to get access token: {data}")
            sys.exit(1)

        self.token = data["access_token"]
        # Set expiration with 5 min buffer
        self.token_expires_at = time.time() + data["expires_in"] - 300

        print(f"✅ Access token obtained")
        return self.token

    def upload_thumb(self, image_path: str) -> str:
        """Upload cover image and return thumb_media_id"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=thumb"

        print(f"📷 Uploading cover image: {image_path}")

        with open(image_path, "rb") as f:
            files = {"media": f}
            response = requests.post(url, files=files)

        data = response.json()

        if "media_id" not in data:
            print(f"❌ Failed to upload cover: {data}")
            sys.exit(1)

        print(f"✅ Cover uploaded: {data['media_id']}")
        return data["media_id"]

    def upload_article_image(self, image_path: str) -> str:
        """Upload image for article content and return URL"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={token}"

        print(f"🖼️ Uploading article image: {image_path}")

        with open(image_path, "rb") as f:
            files = {"media": f}
            response = requests.post(url, files=files)

        data = response.json()

        if "url" not in data:
            print(f"⚠️ Failed to upload article image: {data}")
            return image_path  # Return original path on failure

        print(f"✅ Article image uploaded: {data['url']}")
        return data["url"]

    def create_draft(
        self,
        thumb_media_id: str,
        title: str,
        author: str,
        digest: str,
        content: str,
        content_source_url: str = "",
        need_open_comment: int = 0,
        only_fans_can_comment: int = 0
    ) -> str:
        """Create article draft and return draft media_id"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"

        print("📝 Creating draft...")

        data = {
            "articles": [{
                "title": title,
                "author": author,
                "digest": digest,
                "content": content,
                "content_source_url": content_source_url,
                "thumb_media_id": thumb_media_id,
                "need_open_comment": need_open_comment,
                "only_fans_can_comment": only_fans_can_comment
            }]
        }

        # Use ensure_ascii=False to preserve Chinese characters
        import json
        response = requests.post(
            url,
            data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
            headers={'Content-Type': 'application/json; charset=utf-8'}
        )
        result = response.json()

        if "media_id" not in result:
            print(f"❌ Failed to create draft: {result}")
            sys.exit(1)

        print(f"✅ Draft created: {result['media_id']}")
        return result["media_id"]

    def publish_draft(self, draft_media_id: str) -> Dict:
        """Publish draft and return result"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token={token}"

        print("🚀 Publishing draft...")

        data = {"media_id": draft_media_id}
        # Use ensure_ascii=False to preserve Chinese characters
        import json
        response = requests.post(
            url,
            data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
            headers={'Content-Type': 'application/json; charset=utf-8'}
        )
        result = response.json()

        if result.get("errcode", 0) != 0:
            print(f"❌ Failed to publish: {result}")
            sys.exit(1)

        print(f"✅ Article published successfully!")
        print(f"📌 Publish ID: {result.get('publish_id')}")
        print("\n⚠️ Note: Article is visible in 'View History' but no push notification sent.")

        return result

    def get_publish_status(self, publish_id: str) -> Dict:
        """Check publish status"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/freepublish/get?access_token={token}"

        response = requests.post(url, json={"publish_id": publish_id})
        return response.json()


def load_html_content(html_path: str) -> str:
    """Load HTML content from file"""
    path = Path(html_path)
    if not path.exists():
        print(f"❌ File not found: {html_path}")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser(description="Publish article to WeChat Official Account")
    parser.add_argument("--article", required=True, help="Path to article HTML file")
    parser.add_argument("--title", required=True, help="Article title")
    parser.add_argument("--author", default="技术编辑", help="Author name")
    parser.add_argument("--digest", help="Article summary")
    parser.add_argument("--source-url", default="", help="Original article URL")
    parser.add_argument("--cover", required=True, help="Path to cover image")
    parser.add_argument("--app-id", help="WeChat App ID (or set WECHAT_APP_ID env)")
    parser.add_argument("--app-secret", help="WeChat App Secret (or set WECHAT_APP_SECRET env)")
    parser.add_argument("--open-comment", type=int, default=0, choices=[0, 1],
                       help="Open comments (0=close, 1=open)")
    parser.add_argument("--fans-only", type=int, default=0, choices=[0, 1],
                       help="Fans only comment (0=all, 1=fans)")
    parser.add_argument("--dry-run", action="store_true",
                       help="Validate without actually publishing")

    args = parser.parse_args()

    # Get credentials from args or env
    app_id = args.app_id or os.environ.get("WECHAT_APP_ID")
    app_secret = args.app_secret or os.environ.get("WECHAT_APP_SECRET")

    if not app_id or not app_secret:
        print("❌ WeChat credentials not provided")
        print("Set WECHAT_APP_ID and WECHAT_APP_SECRET environment variables,")
        print("or use --app-id and --app-secret arguments")
        sys.exit(1)

    # Load article content
    print(f"📄 Loading article: {args.article}")
    content = load_html_content(args.article)

    # Auto-generate digest from first 100 chars if not provided
    digest = args.digest
    if not digest:
        # Strip HTML tags for digest
        import re
        text_only = re.sub(r'<[^>]+>', '', content)
        digest = text_only[:100].strip()
        if len(text_only) > 100:
            digest += "..."

    # Initialize publisher
    publisher = WeChatPublisher(app_id, app_secret)

    # Upload cover
    thumb_media_id = publisher.upload_thumb(args.cover)

    if args.dry_run:
        print("\n✅ Dry run completed. Would publish:")
        print(f"  Title: {args.title}")
        print(f"  Author: {args.author}")
        print(f"  Digest: {digest}")
        print(f"  Cover: {thumb_media_id}")
        print(f"  Content length: {len(content)} chars")
        return

    # Create draft
    draft_id = publisher.create_draft(
        thumb_media_id=thumb_media_id,
        title=args.title,
        author=args.author,
        digest=digest,
        content=content,
        content_source_url=args.source_url,
        need_open_comment=args.open_comment,
        only_fans_can_comment=args.fans_only
    )

    # Publish
    result = publisher.publish_draft(draft_id)

    # Check status
    if "publish_id" in result:
        print("\n⏳ Checking publish status...")
        time.sleep(2)  # Wait a bit for status to update
        status = publisher.get_publish_status(result["publish_id"])
        print(f"📊 Status: {status}")


if __name__ == "__main__":
    import os
    main()

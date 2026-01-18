# WeChat Official Account API Guide

Complete guide for publishing articles to WeChat via API.

## Overview

WeChat API publishing uses the **"Draft + Publish"** model:
1. Create article as draft
2. Upload cover image
3. Add article content
4. Publish draft (visible in history, no push notification)

## Prerequisites

### 1. Get AppID and AppSecret

- Login to [WeChat MP Platform](https://mp.weixin.qq.com/)
- Navigate: **设置与开发 → 基本配置** (Settings & Development → Basic Configuration)
- Copy **开发者ID (AppID)** and **开发者密码 (AppSecret)**

### 2. Configure IP Whitelist

- In Basic Configuration page
- Find **IP白名单** (IP Whitelist) section
- Add your server IP address
- Multiple IPs separated by newlines

### 3. Install Dependencies

```bash
npm install axios form-data
# or
pip install requests
```

## API Workflow

### Step 1: Get Access Token

Access token is valid for 2 hours.

```javascript
const axios = require('axios');

async function getAccessToken(appId, appSecret) {
    const url = `https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${appId}&secret=${appSecret}`;
    const res = await axios.get(url);
    return res.data.access_token;
}
```

**Python version**:
```python
import requests

def get_access_token(app_id, app_secret):
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}"
    res = requests.get(url)
    return res.json()['access_token']
```

### Step 2: Upload Cover Image

Cover image must be uploaded as **thumbnail (thumb)** type.

Requirements:
- Format: JPG/PNG
- Size: < 64KB recommended
- Ratio: 2.35:1 (recommended)

```javascript
const FormData = require('form-data');
const fs = require('fs');

async function uploadThumb(token, filePath) {
    const url = `https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=${token}&type=thumb`;
    const form = new FormData();
    form.append('media', fs.createReadStream(filePath));

    const res = await axios.post(url, form, {
        headers: form.getHeaders()
    });

    return res.data.media_id;  // Return thumb_media_id
}
```

**Python version**:
```python
import requests

def upload_thumb(token, file_path):
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=thumb"
    with open(file_path, 'rb') as f:
        files = {'media': f}
        res = requests.post(url, files=files)
    return res.json()['media_id']
```

### Step 3: Create Draft

```javascript
async function addDraft(token, thumbMediaId, articleData) {
    const url = `https://api.weixin.qq.com/cgi-bin/draft/add?access_token=${token}`;

    const data = {
        articles: [{
            title: articleData.title,
            author: articleData.author,
            digest: articleData.digest,        // Summary
            content: articleData.content,       // HTML content
            content_source_url: articleData.sourceUrl,  // Original link
            thumb_media_id: thumbMediaId,
            need_open_comment: articleData.openComment || 0,
            only_fans_can_comment: articleData.fansOnly || 0
        }]
    };

    const res = await axios.post(url, data);
    return res.data.media_id;  // Return draft media_id
}
```

**Article data structure**:
```javascript
const articleData = {
    title: "文章标题",
    author: "作者名",
    digest: "文章摘要，显示在分享链接中",
    content: "<h1>HTML内容</h1><p>支持HTML格式</p>",
    sourceUrl: "https://www.example.com",  // "Read more" link
    openComment: 0,  // 0=close, 1=open
    fansOnly: 0      // 0=all, 1=fans only
};
```

### Step 4: Publish Draft

```javascript
async function publishDraft(token, draftMediaId) {
    const url = `https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token=${token}`;

    const res = await axios.post(url, {
        media_id: draftMediaId
    });

    return res.data;  // Returns { code: 0, msg: "ok", publish_id: "..." }
}
```

## Complete Example

### Node.js Version

```javascript
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

const config = {
    appId: 'YOUR_APPID',
    appSecret: 'YOUR_APPSECRET',
    coverPath: './cover.jpg'
};

async function publishArticle(articleData) {
    try {
        // 1. Get token
        console.log("Getting access token...");
        const token = await getAccessToken(config.appId, config.appSecret);

        // 2. Upload cover
        console.log("Uploading cover image...");
        const thumbId = await uploadThumb(token, config.coverPath);

        // 3. Create draft
        console.log("Creating draft...");
        const draftId = await addDraft(token, thumbId, articleData);

        // 4. Publish
        console.log("Publishing...");
        const result = await publishDraft(token, draftId);

        if (result.errcode === 0 || !result.errcode) {
            console.log("✅ Published successfully!");
            console.log("Publish ID:", result.publish_id);
            console.log("Note: Article is visible in history, but no push notification sent.");
        } else {
            console.error("❌ Publish failed:", result);
        }
    } catch (error) {
        console.error("❌ Error:", error.response ? error.response.data : error.message);
    }
}

// Usage
publishArticle({
    title: "技术周报第52期",
    author: "技术编辑",
    digest: "本周最值得关注的3个技术动态...",
    content: "<h1>技术周报</h1><p>正文内容...</p>",
    sourceUrl: "https://example.com/original"
});
```

### Python Version

See [`scripts/publish_wechat.py`](../scripts/publish_wechat.py) for complete Python implementation.

## Publishing vs Mass Sending

### Publish (freepublish/submit)
- ✅ No daily limit
- ✅ Does not consume mass send quota
- ❌ No push notification to followers
- ✅ Visible in "View History" (查看历史消息)
- ✅ Suitable for: Regular content, article series

### Mass Send (message/mass/sendall)
- ❌ Limited quota (Subscription: 1/day, Service: 4/month)
- ✅ Sends push notification to all followers
- ✅ Higher visibility
- ✅ Suitable for: Important announcements, marketing campaigns

**Note**: Mass send must be used with draft API.

## Status Checking

Check publishing status:

```javascript
async function getPublishStatus(token, publishId) {
    const url = `https://api.weixin.qq.com/cgi-bin/freepublish/get?access_token=${token}`;

    const res = await axios.post(url, { publish_id: publishId });
    return res.data;
}

// Status codes:
// "0" - Success
// "1" - Publishing in progress
// "2" - Failed (need retry)
```

## Image Upload in Article Content

For images inside article body:

```javascript
// Upload article image
async function uploadArticleImage(token, imagePath) {
    const url = `https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=${token}`;
    const form = new FormData();
    form.append('media', fs.createReadStream(imagePath));

    const res = await axios.post(url, form, {
        headers: form.getHeaders()
    });

    return res.data.url;  // Returns image URL
}

// Usage
const imgUrl = await uploadArticleImage(token, './image.jpg');
const htmlContent = `<p>Article content...</p><img src="${imgUrl}" />`;
```

## Error Codes

Common error codes:

| Error Code | Description | Solution |
|------------|-------------|----------|
| 40001 | Invalid credential | Check AppID/AppSecret |
| 40002 | Invalid grant_type | Use `client_credential` |
| 40013 | Invalid AppID | Verify AppID is correct |
| 40164 | IP not in whitelist | Add server IP to whitelist |
| 40006 | Invalid image size | Optimize cover to <64KB |
| 40007 | Invalid media_id | Re-upload image |
| 42001 | Access token expired | Refresh token |
| 45001 | File size exceeds limit | Compress image |
| 85007 | Content review failed | Check content compliance |

## Troubleshooting

### Token Management

```javascript
class TokenManager {
    constructor(appId, appSecret) {
        this.appId = appId;
        this.appSecret = appSecret;
        this.token = null;
        this.expiresAt = null;
    }

    async getToken() {
        if (this.token && Date.now() < this.expiresAt) {
            return this.token;
        }

        const url = `https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${this.appId}&secret=${this.appSecret}`;
        const res = await axios.get(url);

        this.token = res.data.access_token;
        this.expiresAt = Date.now() + (res.data.expires_in - 300) * 1000;  // Refresh 5min early

        return this.token;
    }
}
```

### Debug Mode

```javascript
// Enable detailed logging
axios.interceptors.request.use(config => {
    console.log('📤 Request:', config.method.toUpperCase(), config.url);
    return config;
});

axios.interceptors.response.use(response => {
    console.log('📥 Response:', response.status, response.data);
    return response;
});
```

## Best Practices

1. **Token caching**: Cache tokens with 5-minute buffer before expiration
2. **Image optimization**: Compress images before upload
3. **Error retry**: Implement exponential backoff for retries
4. **Content validation**: Validate HTML before publishing
5. **Status polling**: Poll publish status for confirmation
6. **Logging**: Log all API calls for debugging

## Testing

Use [WeChat Test Account](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login) for testing without affecting your production account.

# Wedding Blessings Moderation Backend (Google Sheets & Apps Script) 🌸💍

This directory contains the Google Apps Script code to enable the 5-step moderation workflow:

```
1. A guest writes a blessing on the website and clicks submit.
2. The blessing is saved in a Google Sheet, but it is hidden. It does not show on the website yet.
3. You get an email saying a new blessing is waiting.
4. You open the Sheet and tick a checkbox next to the blessings you like.
5. Ticked blessings show on the website. Unticked ones stay hidden.
```

---

## 📋 2-Minute Setup Guide

### Step 1: Open Your Google Sheet
1. Open the Google Sheet where your wedding blessings are saved.
2. In the top menu, click **Extensions** > **Apps Script**.

### Step 2: Paste the Updated Code
1. In the Apps Script code editor, delete any existing code.
2. Open [`google-sheets-backend/Code.gs`](./Code.gs) in this repository and copy its entire content.
3. Paste it into the Apps Script editor.
4. *(Optional)* At the top of `Code.gs`, verify or change `NOTIFICATION_EMAILS`:
   ```javascript
   const NOTIFICATION_EMAILS = "akashdubey5450@gmail.com"; 
   // You can also add both emails: "akashdubey5450@gmail.com, pranshi@example.com"
   ```
5. Click the **Save** icon (diskette) or press `Ctrl + S`.

### Step 3: Authorize Email & Sheet Setup (Crucial!)
1. In the Apps Script toolbar, select the function dropdown (where it says `doGet` or `myFunction`).
2. Select **`testEmailNotification`** and click **▷ Run**.
3. When prompted for authorization:
   - Click **Review permissions**.
   - Select your Google account.
   - Click **Advanced** > **Go to Wedding Blessings Backend (unsafe)**.
   - Click **Allow**.
4. Check your Gmail inbox: you will receive a test blessing email!

### Step 4: Deploy the Web App
1. In the top-right corner of Apps Script, click **Deploy** > **Manage deployments**.
2. Click the **Edit** icon (pencil) next to the active deployment.
3. Under **Version**, select **New version**.
4. Ensure:
   - **Execute as**: *Me*
   - **Who has access**: *Anyone*
5. Click **Deploy**.


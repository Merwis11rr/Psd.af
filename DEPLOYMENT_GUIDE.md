# 🚀 GitHub Pages Deployment Guide for PSD.af

## Step-by-Step Deployment Instructions

### 1. Prepare Your Files
Make sure you have these files ready:
```
📁 Your Project Folder
├── index.html
├── brochures.html
├── business-cards.html
├── archive.html
├── contact.html
├── css/
│   └── style.css
├── js/
│   └── main.js
├── README.md
└── DEPLOYMENT_GUIDE.md (this file)
```

### 2. Create GitHub Repository

1. **Go to GitHub.com** and sign in to your account
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Repository name**: Choose a name like `psd-af-portfolio` or `my-design-portfolio`
5. **Description**: "Persian Design Portfolio Website"
6. **Make it Public** (required for free GitHub Pages)
7. **DON'T initialize** with README, .gitignore, or license
8. **Click "Create repository"**

### 3. Upload Your Files

**Option A: Using GitHub Web Interface (Easiest)**
1. **Click "uploading an existing file"** on your new repository page
2. **Drag and drop** all your files and folders
3. **Commit message**: "Initial website upload"
4. **Click "Commit changes"**

**Option B: Using Git Commands**
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
# Copy all your files here
git add .
git commit -m "Initial website upload"
git push origin main
```

### 4. Enable GitHub Pages

1. **Go to your repository** on GitHub
2. **Click "Settings"** tab (at the top of the repository)
3. **Scroll down** to "Pages" in the left sidebar
4. **Click "Pages"**
5. **Under "Source"**, select "Deploy from a branch"
6. **Branch**: Select "main" (or "master")
7. **Folder**: Select "/ (root)"
8. **Click "Save"**

### 5. Access Your Website

- Your website will be available at: `https://yourusername.github.io/repository-name`
- It may take **5-10 minutes** for the first deployment
- You'll see a green checkmark when it's ready

### 6. Update Contact Information

Before going live, update these in ALL HTML files:

**WhatsApp Number:**
- Find: `93123456789`
- Replace with: Your actual WhatsApp number

**Email Address:**
- Find: `info@psd.af`
- Replace with: Your actual email

**Social Media:**
- Update Instagram, Telegram links in the footer

### 7. Customize Your Content

**Homepage (index.html):**
- Update hero section text
- Modify service descriptions
- Change company statistics

**Portfolio Pages:**
- Replace placeholder portfolio items
- Add real project descriptions
- Update project years and categories

**Archive Page:**
- Modify company timeline
- Update testimonials with real client feedback
- Change statistics to match your experience

**Contact Page:**
- Update working hours
- Modify FAQ answers
- Change contact information

### 8. Add Real Images (Optional)

1. **Create an "images" folder** in your repository
2. **Upload your portfolio images**
3. **Update HTML files** to reference real images:
   ```html
   <!-- Replace this: -->
   <div class="placeholder-image">
   
   <!-- With this: -->
   <img src="images/your-image.jpg" alt="Project Name">
   ```

### 9. Custom Domain (Optional)

If you have your own domain:

1. **Create a CNAME file** in your repository root
2. **Add your domain** (e.g., `www.yourwebsite.com`)
3. **In GitHub Pages settings**, add your custom domain
4. **Configure DNS** with your domain provider:
   - CNAME record: `www` → `yourusername.github.io`
   - A records for apex domain:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`

### 🎉 You're Done!

Your Persian design portfolio is now live on the internet! Share your URL with potential clients and showcase your amazing work.

## 🔧 Making Updates

To update your website:
1. **Edit files** in your GitHub repository
2. **Commit changes** with a descriptive message
3. **Wait 2-3 minutes** for changes to appear live

## 📱 Mobile Testing

Test your website on different devices:
- Desktop computers
- Tablets
- Mobile phones
- Different browsers (Chrome, Safari, Firefox, Edge)

## 🆘 Troubleshooting

**Website not loading?**
- Check GitHub Pages settings
- Ensure `index.html` is in root directory
- Wait 10 minutes after enabling Pages

**Images not showing?**
- Check file paths are correct
- Ensure images are uploaded to repository
- Use lowercase filenames without spaces

**Persian text not displaying correctly?**
- Modern browsers support Persian text
- Vazirmatn font loads from Google Fonts
- Check internet connection for font loading

## 📞 Need Help?

If you need assistance with deployment:
- Check GitHub Pages documentation
- Ask in GitHub Community forums
- Contact: info@psd.af

---

**Congratulations on launching your professional design portfolio! 🎨**
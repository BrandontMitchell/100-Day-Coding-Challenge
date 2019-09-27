# Day 050 - Publishing a Personal Website

The purpose of this day is to show you how to put all of your hard work from the previous 9 days on display. You will be publishing your very own personal web page!

## 1. Creating a GitHub account

Click [here](https://github.com/join) to get yourself an account. GitHub offers the free hosting service
that we'll need to publish your website. With your account you'll also be able to view and contribute to other open source projects. You can think of it as a Google Docs for code.

## 2. Download the GitHub Desktop app

### Installation Links

[macOS](https://central.github.com/deployments/desktop/desktop/latest/darwin)

[Windows](https://central.github.com/deployments/desktop/desktop/latest/win32)

If these links don't work, explore the GitHub Desktop homepage [here](https://desktop.github.com/).

We'll be using this app to get the code that you've written uploaded to GitHub. It has a nice
interface that's intuitive to use. Once it's done downloading, open the downloaded file and continue through the installation process.

## 3. Create a new GitHub repository

Before uploading your code to GitHub, we need to first make a **repository**, which is like a big folder
that holds all of the project files.

1. Open the GitHub Desktop app and click the "Create New Repository" Button

2. Fill in the "Name" text input as:

```
[username].github.io
```

3. The "Local Path" text input signifies where your repository will be on your computer (not where the files are
currently located). This must be a new, empty folder.

4. Click the "Create Repository" Button

## 4. Copy your files to the new Repository folder

The folder where all of your files are currently located will be referred to as your **working folder**.
Our next step is to copy all of the files from your working folder to your GitHub Repository folder.

## 5. Commit your Changes

The next step is to **commit** your files. You can think of this as taking a screenshot of your repository
in their current state. When you finally upload the files, GitHub will do some work that compares this
current screenshot with any previously uploaded files. Git is really just a software that compares these
two screenshots and tracks every change that you make.

Before you can commit your changes, GitHub requires a brief description of what you're uploading. This
can come in handy later when you need to remember what you changed, or if you mess something up down the road. Fill in the "Summary" text input located near the bottom left with a high-level description of what new files you're adding. Optionally, you can add more details about the commit in the "Description" text box.

Once these are both filled out, you can click the "Commit to master" button.

## 6. Publish the Website

After clicking the "Commit to master" button in the previous step, all of the files should disappear from
the app interface and there should be a small indicator in the bottom left corner telling you that your
commit was successful.

Now that our files are committed, we can **push** your commit to GitHub. Pushing refers to the process
of uploading your committed files to GitHub.

1. Click the "Publish repository" button. If you haven't already, the GitHub Desktop app will prompt you to log in.

2. Uncheck the "Keep this code private" checkbox. This step is necessary in order for you to share your site with friends and family.

3. Click the "Publish repository" button

## 7. Share your website

This will be the web address you will share when your site is live:

```
https://[username].github.io/
```

Whenever you want to make changes to your website, remember that you need to go through the same process
of committing and pushing your files. Your changes will be published automatically!

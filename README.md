# Automated Email Notification Workflow 📧

A simple GitHub Action workflow that sends an email notification on every push to the `main` branch. This is a learning project to understand repository automation and CI/CD basics.

## How to Use This Workflow

To use this workflow in your own project, you need to set up repository secrets for your email credentials.

1.  **Copy the Workflow File:**
    Create the directory `.github/workflows/` in your project and copy the `email.yml` file from this repository into it.

2.  **Create Repository Secrets:**
    Go to your repository's **Settings > Secrets and variables > Actions** and create the following two secrets:
    * `MAIL_USERNAME`: Your full Gmail address (e.g., `your.email@gmail.com`).
    * `MAIL_PASSWORD`: The 16-character **App Password** you generated from your Google Account settings. **Do not use your regular password.**

3.  **Customize and Push:**
    Optionally, change the `to:` email address inside the workflow file to your own. Commit and push the file, and the action will be active.

## The Workflow Explained

This workflow is configured to run on every push to the `main` branch. It uses the `dawidd6/action-send-mail` action along with your stored secrets to authenticate with the SMTP server and send an email containing details about the latest commit.

## Technology Used

* [GitHub Actions](https://github.com/features/actions)
* [action-send-mail](https://github.com/dawidd6/action-send-mail)
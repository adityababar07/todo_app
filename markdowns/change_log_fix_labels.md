# Change Log: Fixing Visible Labels on Signup/Login

**Date:** 2025-12-10
**Task:** Remove conflicting CSS that was forcing labels to display.

## What I Did
I removed the CSS blocks in `signup.html` and `login.html` that were explicitly setting `display: block` for labels.

## Why I Did It
In a previous step, I added CSS to show labels because placeholders weren't implemented yet. Now that placeholders are correctly added to the forms, this CSS was overriding the default behavior (or my previous attempt to hide them) and causing labels to appear redundantly.

## How I Did It
*   **File**: `templates/signup.html` and `templates/registration/login.html`
*   **Action**: Deleted the following CSS block:
    ```css
    .signup-form label {
        display: block;
        /* ... */
    }
    ```
    (and similarly for `.login-form label`)

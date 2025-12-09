# Change Log: Manual Form Rendering

**Date:** 2025-12-10
**Task:** Convert all forms to manual HTML rendering to ensure placeholders are visible and labels are removed.

## What I Did
I replaced the automatic Django form rendering (e.g., `{{ form.as_p }}` or `{% for field in form %}`) with explicit HTML `<input>` tags for every form in the application.

## Why I Did It
The previous method of using Django widgets and CSS to hide labels and add placeholders was inconsistent and caused issues where labels would reappear or placeholders wouldn't show. Manual rendering gives full control over the HTML structure, ensuring the **Instagram-style** design (no labels, visible placeholders) is applied correctly everywhere.

## How I Did It

### 1. Signup Page (`templates/signup.html`)
*   Replaced `{{ form.as_p }}` with manual inputs for:
    *   `email` (Email)
    *   `name` (Full Name)
    *   `username` (Username)
    *   `password` (Password)

### 2. Create/Edit Post (`templates/todo_new.html`, `templates/todo_edit.html`)
*   Replaced the field loop with manual inputs for:
    *   `title` (Text Input)
    *   `category` (Select Dropdown)
    *   `body` (Textarea)
*   Added logic to pre-fill values in the Edit form using `value="{{ form.field.value }}"`.

### 3. Edit Profile (`templates/profile_edit.html`)
*   Replaced `{{ form.as_p }}` with manual inputs for all 11 profile fields.
*   Added logic to pre-fill existing values.

### 4. Login Page (`templates/registration/login.html`)
*   (Already manually rendered in a previous step, verified consistency).
